import grpc
from earth_service_pb2_grpc import EarthServiceStub
from earth_service_pb2 import GetAllCountriesRequest

channel = grpc.insecure_channel("localhost:8080")
stub = EarthServiceStub(channel)

all_countries = stub.GetAllCountries(
    GetAllCountriesRequest(
        message="Hello server",
    )
)

print(all_countries)