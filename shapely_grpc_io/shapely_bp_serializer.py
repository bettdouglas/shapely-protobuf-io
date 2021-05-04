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
import shapely_grpc_io.geometry as gbp
from shapely.errors import DimensionError


class ShapelyBPSerializer:

    def serialize(self,g: BaseGeometry) -> gbp.Geometry:
        geom_type = type(g)

        if geom_type is Point:
            return self.serialize_point(g)
        elif geom_type is LineString:
            return self.serialize_linestring(g)
        elif geom_type is LinearRing:
            return self.serialize_linearing(g)
        elif geom_type is Polygon:
            return self.serialize_polygon(g)
        elif geom_type is MultiPoint:
            return self.serialize_multi_point(g)
        elif geom_type is MultiPolygon:
            return self.serialize_multi_polygon(g)
        elif geom_type == MultiLineString:
            return self.serialize_multi_linestring(g)
        elif geom_type == GeometryCollection:
            return self.serialize_geometry_collection(g)
        raise NotImplementedError(g)
        
    def serialize_point(self, p: Point) -> gbp.Geometry:
        try:
            coordinate = gbp.Coordinate(x=p.x, y=p.y, z=p.z, has_z=True)
        except DimensionError:
            coordinate = gbp.Coordinate(x=p.x, y=p.y, has_z=False)

        return gbp.Geometry(type=gbp.Type.POINT,coordinates=[coordinate])

    def serialize_linestring(self, l: LineString) -> gbp.Geometry:
        coords = [self.create_coordinate_from_tuple(coord) for coord in list(l.coords)]
        return gbp.Geometry(type=gbp.Type.LINESTRING, coordinates=coords)

    def serialize_linearing(self, l: LinearRing):
        coords = [self.create_coordinate_from_tuple(coord) for coord in list(l.coords)]
        return gbp.Geometry(type=gbp.Type.LINEARRING, coordinates=coords)

    def create_coordinate_from_tuple(self, coordinates) -> gbp.Coordinate:
        try:
            return gbp.Coordinate(
                x=coordinates[0],
                y=coordinates[1],
                z=coordinates[2],
                has_z=True,
            )
        except IndexError:
            return gbp.Coordinate(
                x=coordinates[0],
                y=coordinates[1],
                has_z=False,
            )

    def serialize_polygon(self, geometry: Polygon) -> gbp.Geometry:
        # get outer ring
        exterior_linestring = geometry.exterior
        # get inner linear rings
        interior_rings = geometry.interiors

        exterior_coords = [
            self.create_coordinate_from_tuple(coord)
            for coord in list(exterior_linestring.coords)
        ]
        external_geo = gbp.Geometry(coordinates=exterior_coords)

        geo_polygon = None

        if len(interior_rings) > 0:
            interior_geometries = []
            for linear_ring in interior_rings:
                ring_coords = [
                    self.create_coordinate_from_tuple(coord)
                    for coord in linear_ring.coords
                ]
                iGeo = gbp.Geometry(
                    coordinates=ring_coords,
                )
                interior_geometries.append(iGeo)
            interiorGeos = gbp.Geometry(
                geometries=interior_geometries,
            )
            geo_polygon = gbp.Geometry(
                type=gbp.Type.POLYGON, geometries=[external_geo, interiorGeos]
            )
        else:
            geo_polygon = gbp.Geometry(type=gbp.Type.POLYGON, geometries=[external_geo])

        return geo_polygon

    def serialize_multi_point(self, mp: MultiPoint):
        return gbp.Geometry(
            type=gbp.Type.MULTIPOINT,
            geometries=[self.serialize_point(point) for point in mp.geoms],
        )

    def serialize_multi_linestring(self, ls: MultiLineString):
        return gbp.Geometry(
            type=gbp.Type.MULTILINESTRING,
            geometries=[self.serialize_linestring(line) for line in ls.geoms],
        )

    def serialize_multi_polygon(self, mp: MultiPolygon):
        return gbp.Geometry(
            type=gbp.Type.MULTIPOLYGON,
            geometries=[self.serialize_polygon(p) for p in mp.geoms],
        )

    def serialize_geometry_collection(self, gc: GeometryCollection):
        geometries = [self.serialize(geom) for geom in gc.geoms]
        return gbp.Geometry(
            type=gbp.Type.GEOMETRYCOLLECTION,
            geometries=geometries,
        )