from shapely_serializer import ShapelyGeometrySerializer
from shapely_deserializer import ShapelyPBDeserializer

from kenya_wards_pb2 import (
    Level1Boundary,
    Level2Boundary,
    BoundariesRequest,
    Level1BoundariesResponse,
    Level2BoundariesResponse,
)

from kenya_wards_pb2_grpc import (
    AdminBoundariesServiceServicer,
    add_AdminBoundariesServiceServicer_to_server,
)

import geopandas as gpd
import os
# from shapely_grpc_io import pb_toshapely_deserializer, shapely_topb_serializer
import grpc
from concurrent import futures

pb_toshapely_deserializer = ShapelyPBDeserializer()
shapely_topb_serializer = ShapelyGeometrySerializer()

class AdminBoundariesServicer(AdminBoundariesServiceServicer):
    def __init__(self) -> None:
        # 
        self.adm1_gdf = gpd.read_file("example/data/adm1.gpkg")
        self.adm2_gdf = gpd.read_file("example/data/adm2.gpkg")

    def GetLevel1Boundaries(self, request, context):
        print(request)
        boundaries = [to_level1(row) for _, row in self.adm1_gdf.iterrows()]

        return Level1BoundariesResponse(
            boundaries=boundaries,
        )

    def GetLevel2Boundaries(self, request, context):
        print(request)
        boundaries = [to_level2(row) for _, row in self.adm2_gdf.iterrows()]

        return Level2BoundariesResponse(boundaries=boundaries)


def to_level1(row) -> Level1Boundary:
    return Level1Boundary(
        code=row["code"],
        name=row["name"],
        boundary=shapely_topb_serializer.serialize(row["geometry"]),
    )


def to_level2(row) -> Level2Boundary:
    return Level2Boundary(
        id=row["code"],
        name=row["name"],
        adm1name=row["admin1_name"],
        boundary=shapely_topb_serializer.serialize(row["geometry"]),
    )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_AdminBoundariesServiceServicer_to_server(AdminBoundariesServicer(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()