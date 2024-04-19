import grpc
from google.protobuf.json_format import MessageToDict
from api.pb.flight_pb2 import FlightRequest, FlightClass, FlightFood, FlightLuggage
from api.pb.flight_pb2_grpc import FlightStub

import config


class FlightClient:
    def __init__(self):
        self._channel = grpc.insecure_channel(f"{config.settings.grpc_flight}:50052")
        self._stub = FlightStub(self._channel)

    def get_flight(self, flight):
        try:
            stub = self._stub.GetFlight(FlightRequest(
                    class_=FlightClass(value=flight.class_),
                    food=FlightFood(value=flight.food),
                    luggage=FlightLuggage(
                        checked=flight.luggage.checked,
                        quantity=flight.luggage.quantity
                    )
                )
            )

            return MessageToDict(
                stub,
                preserving_proto_field_name=True,
                including_default_value_fields=True
            )

        except grpc.RpcError as rpc_error:
            return {
                "flight_data": rpc_error.details()
            }