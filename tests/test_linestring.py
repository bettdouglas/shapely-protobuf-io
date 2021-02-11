from shapely_grpc_io import (
    shapely_topb_serializer as topb,
    pb_toshapely_deserializer as to_shapely,
)
from shapely.geometry import LineString
from shapely_grpc_io import geometry_pb2 as pb2


def test_linestring_serialization():
    line = LineString(((1.0, 2.0), (3.0, 4.0)))

    line_proto = topb.serialize(line)

    deserialized = to_shapely.deserialize(line_proto)

    assert type(deserialized) is LineString

    assert line.equals(deserialized)


def test_coordinate_order_preservation():
    line = LineString(((1.0, 2.0), (3.0, 4.0)))

    line_proto = topb.serialize(line)

    deserialized = to_shapely.deserialize(line_proto)

    assert len(deserialized.coords) == 2
    assert deserialized.coords[:] == [(1.0, 2.0), (3.0, 4.0)]


def test_3d_linestring():
    line = LineString(((1.0, 2.0, 3.0), (3.0, 4.0, 5.0)))

    line_proto = topb.serialize(line)

    deserialized = to_shapely.deserialize(line_proto)
    assert type(deserialized) is LineString

    assert deserialized.coords[:] == [(1.0, 2.0, 3.0), (3.0, 4.0, 5.0)]
