import get_data_entry_pb2_grpc
import get_data_entry_pb2

import time
import grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = get_data_entry_pb2_grpc.DataEntryGetterStub(channel)
        get_data_entry_request = get_data_entry_pb2.GetDataEntryRequest(
            dataset_id="63559be195234a9215e884bc"
        )
        get_data_entry_reply = stub.GetDataEntry(get_data_entry_request)
        print(get_data_entry_reply.data_type)


if __name__ == "__main__":
    run()
