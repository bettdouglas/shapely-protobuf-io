from shapely_grpc_io import (
    shapely_betterproto_serializer as topb,
    shapely_betterproto_deserializer as to_shapely,
)
from shapely.geometry import MultiPoint


def test_multipoint():
    geom = MultiPoint(((1.0, 2.0), (3.0, 4.0)))

    multipoint_proto = topb.serialize(geom)

    deserialized = to_shapely.deserialize(multipoint_proto)

    assert type(deserialized) is MultiPoint

    assert len(deserialized.geoms) == 2


def test_multipoint_3d():
    geom = MultiPoint(((1.0, 2.0, 4.0), (3.0, 4.0, 5.0)))

    multipoint_proto = topb.serialize(geom)

    deserialized = to_shapely.deserialize(multipoint_proto)

    assert type(deserialized) is MultiPoint

    assert deserialized.geoms[0].x == 1.0
    assert deserialized.geoms[0].y == 2.0
    assert deserialized.geoms[0].z == 4.0
    assert deserialized.equals(geom)

    assert deserialized.geoms[1].x == 3.0
    assert deserialized.geoms[1].y == 4.0
    assert deserialized.geoms[1].z == 5.0


def test_emtpy_multipoint():
    geom = MultiPoint()

    multipoint_proto = topb.serialize(geom)

    deserialized = to_shapely.deserialize(multipoint_proto)

    assert type(deserialized) is MultiPoint

    assert deserialized.equals(geom)
