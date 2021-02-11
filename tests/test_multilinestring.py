from shapely_grpc_io import (
    shapely_topb_serializer as topb,
    pb_toshapely_deserializer as to_shapely,
)
from shapely.geometry import MultiLineString, LineString


def test_multilinestring_serialization():
    geom = MultiLineString((((1.0, 2.0), (3.0, 4.0)),))

    multiline_proto = topb.serialize(geom)

    deserialized = to_shapely.deserialize(multiline_proto)

    assert type(deserialized) is MultiLineString

    assert deserialized.equals(geom)


def test_multilinestring_individual_lines():
    line0 = LineString([(0.0, 1.0), (2.0, 3.0)])
    line1 = LineString([(4.0, 5.0), (6.0, 7.0)])

    multi = MultiLineString([line0, line1])

    multiline_proto = topb.serialize(multi)

    deserialized = to_shapely.deserialize(multiline_proto)

    assert multi.geoms[:] == deserialized.geoms[:]

    # wkt = MultiLineString([LineString([(0, 0), (1, 1), (2, 2)]), LineString()])
