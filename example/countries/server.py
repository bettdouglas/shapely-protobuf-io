from earth_service_pb2_grpc import (
    EarthServiceServicer,
    add_EarthServiceServicer_to_server,
)
from earth_service_pb2 import Countries, Country
import geopandas as gpd
import logging


class EarthService(EarthServiceServicer):
    def __init__(self, countries_fp) -> None:
        gdf = gpd.read_file(countries_fp)
        self.gdf = gdf[["TYPE", "ADMIN", "geometry", "ADM0_A3"]]
        self.gdf = gpd.read_file(countries_fp)

    def GetAllCountries(self, request, context):
        logging.info(f"GetAllCountries {request}")
        return rows_to_countries(self.gdf)

    def SearchCountries(self, request, context):
        logging.info(f"SearchCountries {request}")
        filter = request.keyword
        subset = self.gdf.loc[self.gdf["ADMIN"].str.contains(filter)]
        return rows_to_countries(subset)

    def GetCountriesInBoundary(self, request, context):
        logging.info(f"GetCountriesInBoundary {request}")
        bounds = request.boundary
        shapely_bounds = deserialize_protobuf_geometry(bounds)
        subset = self.gdf.loc[self.gdf.geometry.intersects(shapely_bounds)]
        return rows_to_countries(subset)


from serializers import ShapelyGeometrySerializer

serializer = ShapelyGeometrySerializer()


def row_to_country(row):
    return Country(
        name=row["ADMIN"],
        type=row["TYPE"],
        geometry=serializer.serialize(row["geometry"]),
        code=row["ADM0_A3"],
    )


def rows_to_countries(gdf):
    return Countries(countries=[row_to_country(row) for _, row in gdf.iterrows()])


from serializers import ShapelyPBDeserializer

deserializer = ShapelyPBDeserializer()


def deserialize_protobuf_geometry(serialized_geometry):
    geometry = deserializer.deserialize(serialized_geometry)
    return geometry


from concurrent import futures
import grpc
import os

def _serve(port):
    server = grpc.server(futures.ThreadPoolExecutor())
    filename = 'ne_110m_admin_0_countries.zip'
    if not os.path.exists(filename):
        import wget
        url = "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/ne_110m_admin_0_countries.zip"
        # download countries_data set
        filename = wget.download(url)

    add_EarthServiceServicer_to_server(
        servicer=EarthService(filename),
        server=server,
    )

    bind_address = f"[::]:{port}"
    server.add_insecure_port(bind_address)

    server.start()
    logging.info("Listening on %s.", bind_address)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    _serve(8080)
