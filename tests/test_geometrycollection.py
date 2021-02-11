from shapely.geometry.collection import GeometryCollection
from shapely_grpc_io import (
    shapely_topb_serializer as topb,
    pb_toshapely_deserializer as to_shapely,
)
from shapely.geometry import (
    LineString,
    Point,
    MultiLineString,
    LinearRing,
    GeometryCollection,
)
from shapely_grpc_io import geometry_pb2 as pb2

line = LineString(((1.0, 2.0), (3.0, 4.0)))
p = Point(1.0, 2.0, 3.0)
geom = MultiLineString((((1.0, 2.0), (3.0, 4.0)),))
ring = LinearRing(((0.0, 0.0), (0.0, 1.0), (1.0, 1.0)))


def test_geometrycollection_serialization():
    coll = GeometryCollection([p, geom, ring])

    coll_proto = topb.serialize(coll)

    deserialized = to_shapely.deserialize(coll_proto)

    assert type(deserialized) is GeometryCollection

    assert deserialized.equals(coll)


def test_geometrycollection_in_geometrycollection():

    coll = GeometryCollection([p, geom, ring])

    coll2 = GeometryCollection([coll, p, geom, ring])

    coll2_proto = topb.serialize(coll2)

    deserialized2 = to_shapely.deserialize(coll2_proto)

    assert type(deserialized2) is GeometryCollection

    assert deserialized2.equals(coll2)
