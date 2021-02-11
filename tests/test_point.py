from shapely_grpc_io import (
    shapely_topb_serializer as topb,
    pb_toshapely_deserializer as to_shapely,
)
from shapely.geometry import Point
from shapely_grpc_io import geometry_pb2 as pb2
import pytest


def test_point_serialization():
    p = Point(1.0, 2.0)

    point_proto = topb.serialize(p)

    assert point_proto.type == pb2.POINT

    coords = point_proto.coordinates
    assert len(coords) == 1

    p1 = to_shapely.deserialize(point_proto)

    assert p1.coords[:] == [(1.0, 2.0)]
    assert p1.has_z is False

    assert type(p1) is Point


def test_empty_coordinate():
    p = Point()

    with pytest.raises(IndexError):
        topb.serialize(p)


def test_point_3d():
    p = Point(1.0, 2.0, 3.0)

    point_proto = topb.serialize(p)

    deserialized = to_shapely.deserialize(point_proto)

    assert deserialized.coords[:] == [(1.0, 2.0, 3.0)]
