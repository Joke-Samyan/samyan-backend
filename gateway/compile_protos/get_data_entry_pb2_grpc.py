# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import compile_protos.get_data_entry_pb2 as get__data__entry__pb2


class DataEntryGetterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDataEntry = channel.unary_unary(
                '/get_data.DataEntryGetter/GetDataEntry',
                request_serializer=get__data__entry__pb2.GetDataEntryRequest.SerializeToString,
                response_deserializer=get__data__entry__pb2.GetDataEntryResponse.FromString,
                )


class DataEntryGetterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetDataEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataEntryGetterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDataEntry': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDataEntry,
                    request_deserializer=get__data__entry__pb2.GetDataEntryRequest.FromString,
                    response_serializer=get__data__entry__pb2.GetDataEntryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'get_data.DataEntryGetter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataEntryGetter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetDataEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/get_data.DataEntryGetter/GetDataEntry',
            get__data__entry__pb2.GetDataEntryRequest.SerializeToString,
            get__data__entry__pb2.GetDataEntryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
