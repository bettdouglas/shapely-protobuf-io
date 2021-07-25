from shapely.geometry import (
    Point,
    LineString,
    LinearRing,
    Polygon,
    MultiPoint,
    MultiPolygon,
    MultiLineString,
)
from shapely.geometry.base import BaseGeometry
from shapely.geometry.collection import GeometryCollection
import geometry_pb2 as gpb
from shapely.errors import DimensionError


class ShapelyGeometrySerializer:
    """
    Serializes shapely geometries to geoprotobuf geometries
    """

    def serialize(self, geometry: BaseGeometry) -> gpb.Geometry:
        geom_type = type(geometry)

        if geom_type is Point:
            return self.serialize_point(geometry)
        if geom_type is LineString:
            return self.serialize_linestring(geometry)
        if geom_type is LinearRing:
            return self.serialize_linearing(geometry)
        if geom_type is Polygon:
            return self.serialize_polygon(geometry)
        if geom_type is MultiPoint:
            return self.serialize_multi_point(geometry)
        if geom_type is MultiLineString:
            return self.serialize_multi_linestring(geometry)
        if geom_type is MultiPolygon:
            return self.serialize_multi_polygon(geometry)
        if geom_type is GeometryCollection:
            return self.serialize_geometry_collection(geometry)

    def serialize_point(self, p: Point) -> gpb.Geometry:
        try:
            coordinate = gpb.Coordinate(x=p.x, y=p.y, z=p.z, has_z=True)
        except DimensionError:
            coordinate = gpb.Coordinate(x=p.x, y=p.y, has_z=False)

        return gpb.Geometry(type=gpb.Type.POINT, coordinates=[coordinate])

    def serialize_linestring(self, l: LineString):
        coords = [self.create_coordinate_from_tuple(coord) for coord in list(l.coords)]
        return gpb.Geometry(type=gpb.Type.LINESTRING, coordinates=coords)

    def serialize_linearing(self, l: LinearRing):
        coords = [self.create_coordinate_from_tuple(coord) for coord in list(l.coords)]
        return gpb.Geometry(type=gpb.Type.LINEARRING, coordinates=coords)

    def create_coordinate_from_tuple(self, coordinates) -> gpb.Coordinate:
        try:
            return gpb.Coordinate(
                x=coordinates[0],
                y=coordinates[1],
                z=coordinates[2],
                has_z=True,
            )
        except IndexError:
            return gpb.Coordinate(
                x=coordinates[0],
                y=coordinates[1],
                has_z=False,
            )

    def serialize_polygon(self, geometry: Polygon) -> gpb.Geometry:
        # get outer ring
        exterior_linestring = geometry.exterior
        # get inner linear rings
        interior_rings = geometry.interiors

        exterior_coords = [
            self.create_coordinate_from_tuple(coord)
            for coord in list(exterior_linestring.coords)
        ]
        external_geo = gpb.Geometry(coordinates=exterior_coords)

        geo_polygon = None

        if len(interior_rings) > 0:
            interior_geometries = []
            for linear_ring in interior_rings:
                ring_coords = [
                    self.create_coordinate_from_tuple(coord)
                    for coord in linear_ring.coords
                ]
                iGeo = gpb.Geometry(
                    coordinates=ring_coords,
                )
                interior_geometries.append(iGeo)
            interiorGeos = gpb.Geometry(
                geometries=interior_geometries,
            )
            geo_polygon = gpb.Geometry(
                type=gpb.Type.POLYGON, geometries=[external_geo, interiorGeos]
            )
        else:
            geo_polygon = gpb.Geometry(type=gpb.Type.POLYGON, geometries=[external_geo])

        return geo_polygon

    def serialize_multi_point(self, mp: MultiPoint):
        return gpb.Geometry(
            type=gpb.Type.MULTIPOINT,
            geometries=[self.serialize_point(point) for point in mp.geoms],
        )

    def serialize_multi_linestring(self, ls: MultiLineString):
        return gpb.Geometry(
            type=gpb.Type.MULTILINESTRING,
            geometries=[self.serialize_linestring(line) for line in ls.geoms],
        )

    def serialize_multi_polygon(self, mp: MultiPolygon):
        return gpb.Geometry(
            type=gpb.Type.MULTIPOLYGON,
            geometries=[self.serialize_polygon(p) for p in mp.geoms],
        )

    def serialize_geometry_collection(self, gc: GeometryCollection):
        geometries = [self.serialize(geom) for geom in gc.geoms]
        return gpb.Geometry(
            type=gpb.Type.GEOMETRYCOLLECTION,
            geometries=geometries,
        )


class ShapelyPBDeserializer:
    """
    This class provides the JTS to ProtoBuf Deserialization functionality.
    """

    def deserialize(self, gpbGeometry: gpb.Geometry) -> BaseGeometry:
        enum_type = gpbGeometry.type
        if enum_type == gpb.Type.POINT:
            return self.deserialize_point(gpbGeometry)
        elif enum_type == gpb.Type.LINESTRING:
            return self.deserialize_line(gpbGeometry)
        elif enum_type == gpb.Type.LINEARRING:
            return self.deserialize_linear_ring(gpbGeometry)
        elif enum_type == gpb.Type.POLYGON:
            return self.deserialize_polygon(gpbGeometry)
        elif enum_type == gpb.Type.MULTIPOINT:
            return self.deserialize_multi_point(gpbGeometry)
        elif enum_type == gpb.Type.MULTILINESTRING:
            return self.deserialize_multi_linestring(gpbGeometry)
        elif enum_type == gpb.Type.MULTIPOLYGON:
            return self.deserialize_multi_polygon(gpbGeometry)
        elif enum_type == gpb.Type.GEOMETRYCOLLECTION:
            return self.deserialize_geometry_collection(gpbGeometry)
        elif enum_type == gpb.Type.TRIANGLE:
            # returns shapely Polygon
            return self.deserialize_triangle(gpbGeometry)
        elif enum_type == gpb.Type.LINE:
            # returns linestring
            return self.deserialize_line(gpbGeometry)

    def deserialize_point(self, gpbGeometry) -> Point:
        return self.coordinate_to_point(gpbGeometry.coordinates[0])

    def deserialize_line(self, gpbGeometry) -> LineString:
        points = [self.coordinate_to_point(coord) for coord in gpbGeometry.coordinates]
        return LineString(points)

    def deserialize_linear_ring(self, gpbGeometry) -> LinearRing:
        points = [self.coordinate_to_point(coord) for coord in gpbGeometry.coordinates]
        return LinearRing(points)

    def deserialize_polygon(self, gpbGeometry) -> Polygon:
        geometries_count = len(gpbGeometry.geometries)
        if geometries_count == 0:
            raise "Polygon has no geometries"
        elif geometries_count == 1:
            exterior_ls = gpbGeometry.geometries[0]
            points = [
                self.coordinate_to_point(coord) for coord in exterior_ls.coordinates
            ]
            return Polygon(points)
        else:
            exterior_ls = gpbGeometry.geometries[0]
            exterior_ls_coordinates = [
                self.coordinate_to_point(coord) for coord in exterior_ls.coordinates
            ]

            interior_linear_rings_gpb = gpbGeometry.geometries[1].geometries

            interior_linear_rings = []
            for ring in interior_linear_rings_gpb:
                interior_linear_rings.append(
                    self.gpb_coords_to_xyz_tuples(ring.coordinates)
                )
            return Polygon(exterior_ls_coordinates, interior_linear_rings)

    def deserialize_multi_point(self, gpbGeometry) -> MultiPoint:
        points = [
            self.deserialize_point(geometry) for geometry in gpbGeometry.geometries
        ]
        return MultiPoint(points)

    def deserialize_multi_linestring(self, gpbGeometry) -> MultiLineString:
        lines = [self.deserialize_line(geometry) for geometry in gpbGeometry.geometries]
        return MultiLineString(lines)

    def deserialize_multi_polygon(self, gpbGeometry) -> MultiPolygon:
        polygons = [
            self.deserialize_polygon(geometry) for geometry in gpbGeometry.geometries
        ]
        return MultiPolygon(polygons)

    def deserialize_geometry_collection(self, gpbGeometry) -> GeometryCollection:
        geometries = [
            self.deserialize_geometry(geometry) for geometry in gpbGeometry.geometries
        ]
        return GeometryCollection(geometries)

    def deserialize_geometry(self, gpbGeometry) -> BaseGeometry:
        geom_type = gpbGeometry.type
        if geom_type == gpb.Type.POINT:
            return self.deserialize_point(gpbGeometry)
        elif geom_type == gpb.Type.LINESTRING:
            return self.deserialize_line(gpbGeometry)
        elif geom_type == gpb.Type.POLYGON:
            return self.deserialize_polygon(gpbGeometry)
        elif geom_type == gpb.Type.MULTIPOINT:
            return self.deserialize_multi_point(gpbGeometry)
        elif geom_type == gpb.Type.MULTILINESTRING:
            return self.deserialize_multi_linestring(gpbGeometry)
        elif geom_type == gpb.Type.MULTIPOLYGON:
            return self.deserialize_multi_linestring(gpbGeometry)
        elif geom_type == gpb.Type.LINEARRING:
            return self.deserialize_linear_ring(gpbGeometry)
        elif geom_type == gpb.Type.GEOMETRYCOLLECTION:
            return self.deserialize_geometry_collection(gpbGeometry)
        else:
            raise "{} unsupported for geometric deserialization".format(geom_type)

    def deserialize_triangle(self, geometry: gpb.Geometry):
        coordinates = geometry.coordinates
        return Polygon(
            shell=[self.gpb_coords_to_xyz_tuples(coord) for coord in coordinates]
        )

    def coordinate_to_point(self, coord: gpb.Coordinate) -> Point:
        return Point(self.coord_as_tuple(coord))

    def gpb_coords_to_xyz_tuples(self, gpb_coords):
        return [self.coord_as_tuple(coord) for coord in gpb_coords]

    def coord_as_tuple(self, coord: gpb.Coordinate) -> tuple:
        if coord.has_z:
            return (coord.x, coord.y, coord.z)
        else:
            return (coord.x, coord.y)
