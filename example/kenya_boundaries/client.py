import grpc
from kenya_wards_pb2_grpc import AdminBoundariesServiceStub
from kenya_wards_pb2 import BoundariesRequest

channel = grpc.insecure_channel("[::]:50051",options=(('grpc.so_reuseport', 0),))
client = AdminBoundariesServiceStub(channel)

response = client.GetLevel1Boundaries(BoundariesRequest())

print(response.response)