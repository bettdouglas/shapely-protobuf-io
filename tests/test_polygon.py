from shapely_grpc_io import (
    shapely_topb_serializer as topb,
    pb_toshapely_deserializer as to_shapely,
)
from shapely.geometry import Polygon


def test_polygon_serialization():
    coords = [(0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (0.0, 0.0)]

    polygon = Polygon(((0.0, 0.0), (0.0, 1.0), (1.0, 1.0)))

    polygon_proto = topb.serialize(polygon)

    deserialized = to_shapely.deserialize(polygon_proto)

    assert type(deserialized) is Polygon

    assert deserialized.equals(polygon)

    assert deserialized.exterior.coords[:] == coords


def test_polygonwith_holes():
    coords = [(0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (0.0, 0.0)]

    polygon = Polygon(coords, [((0.25, 0.25), (0.25, 0.5), (0.5, 0.5), (0.5, 0.25))])

    polygon_proto = topb.serialize(polygon)

    deserialized = to_shapely.deserialize(polygon_proto)

    assert deserialized.exterior.coords[:] == coords

    assert len(deserialized.interiors[0].coords) == 5


def test_polygon_empty():
    polygon = Polygon()

    polygon_proto = topb.serialize(polygon)

    deserialized = to_shapely.deserialize(polygon_proto)

    assert type(deserialized) is Polygon

    assert deserialized.equals(polygon)
