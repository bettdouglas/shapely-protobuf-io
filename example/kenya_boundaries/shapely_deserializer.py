from shapely import geometry
from shapely.geometry import (
    LineString,
    Point,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    LinearRing,
    Polygon,
    GeometryCollection,
)
from shapely.geometry.base import BaseGeometry
import geometry_pb2 as gpb


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
