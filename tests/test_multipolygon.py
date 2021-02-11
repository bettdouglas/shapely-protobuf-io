from shapely_grpc_io import (
    shapely_topb_serializer as topb,
    pb_toshapely_deserializer as to_shapely,
)
from shapely.geometry import MultiPolygon, LinearRing


def test_multipolygon():
    geom = MultiPolygon(
        [
            (
                ((0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0)),
                [((0.25, 0.25), (0.25, 0.5), (0.5, 0.5), (0.5, 0.25))],
            )
        ]
    )

    multipolygon_proto = topb.serialize(geom)

    deserialized = to_shapely.deserialize(multipolygon_proto)

    assert type(deserialized) is MultiPolygon

    assert deserialized.equals(geom)


def test_empty_multipolygon():
    geom = MultiPolygon()

    multipolygon_proto = topb.serialize(geom)

    deserialized = to_shapely.deserialize(multipolygon_proto)

    assert deserialized.equals(geom)
