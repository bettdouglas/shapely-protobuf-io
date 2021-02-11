from shapely_grpc_io import (
    shapely_topb_serializer as topb,
    pb_toshapely_deserializer as to_shapely,
)
from shapely.geometry import LinearRing
from shapely_grpc_io import geometry_pb2 as pb2
import pytest


def test_linearring_serialization():
    expected_coords = [(0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (0.0, 0.0)]

    ring = LinearRing(((0.0, 0.0), (0.0, 1.0), (1.0, 1.0)))

    ring_proto = topb.serialize(ring)

    deserialized = to_shapely.deserialize(ring_proto)

    assert deserialized.coords[:] == expected_coords


def test_empty_linearing():
    ring = LinearRing()

    ring_proto = topb.serialize(ring)

    # with pytest.raises(BaseException):
    deserialized = to_shapely.deserialize(ring_proto)

    assert deserialized.equals(ring)
