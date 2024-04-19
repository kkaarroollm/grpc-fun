import json

import grpc
from google.protobuf.json_format import MessageToDict
from api.pb.hotel_pb2 import HotelRequest
from api.pb.hotel_pb2_grpc import HotelStub

import config


class HotelClient:
    def __init__(self):
        self._channel = grpc.insecure_channel(f"{config.settings.grpc_hotel}:50051")
        self._stub = HotelStub(self._channel)

    def get_hotel(self, hotel):
        try:
            stub = self._stub.GetHotel(HotelRequest(
                stars=hotel.stars,
                all_inclusive=True,
                room_service=True,
                airport_shuttle=True)
            )

            return MessageToDict(
                stub,
                preserving_proto_field_name=True,
                including_default_value_fields=True
            )

        except grpc.RpcError as rpc_error:
            return {
                "hotel_data": rpc_error.details()
            }
