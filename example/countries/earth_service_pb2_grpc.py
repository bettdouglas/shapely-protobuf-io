# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import earth_service_pb2 as earth__service__pb2


class EarthServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllCountries = channel.unary_unary(
                '/countries.EarthService/GetAllCountries',
                request_serializer=earth__service__pb2.GetAllCountriesRequest.SerializeToString,
                response_deserializer=earth__service__pb2.Countries.FromString,
                )
        self.SearchCountries = channel.unary_unary(
                '/countries.EarthService/SearchCountries',
                request_serializer=earth__service__pb2.SearchCountriesRequest.SerializeToString,
                response_deserializer=earth__service__pb2.Countries.FromString,
                )
        self.GetCountriesInBoundary = channel.unary_unary(
                '/countries.EarthService/GetCountriesInBoundary',
                request_serializer=earth__service__pb2.GetCountriesInBoundaryRequest.SerializeToString,
                response_deserializer=earth__service__pb2.Countries.FromString,
                )


class EarthServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllCountries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchCountries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCountriesInBoundary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EarthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllCountries': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllCountries,
                    request_deserializer=earth__service__pb2.GetAllCountriesRequest.FromString,
                    response_serializer=earth__service__pb2.Countries.SerializeToString,
            ),
            'SearchCountries': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchCountries,
                    request_deserializer=earth__service__pb2.SearchCountriesRequest.FromString,
                    response_serializer=earth__service__pb2.Countries.SerializeToString,
            ),
            'GetCountriesInBoundary': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCountriesInBoundary,
                    request_deserializer=earth__service__pb2.GetCountriesInBoundaryRequest.FromString,
                    response_serializer=earth__service__pb2.Countries.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'countries.EarthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EarthService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllCountries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/countries.EarthService/GetAllCountries',
            earth__service__pb2.GetAllCountriesRequest.SerializeToString,
            earth__service__pb2.Countries.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchCountries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/countries.EarthService/SearchCountries',
            earth__service__pb2.SearchCountriesRequest.SerializeToString,
            earth__service__pb2.Countries.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCountriesInBoundary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/countries.EarthService/GetCountriesInBoundary',
            earth__service__pb2.GetCountriesInBoundaryRequest.SerializeToString,
            earth__service__pb2.Countries.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
