from pb.flight_pb2 import FlightResponse
from pb.flight_pb2_grpc import FlightServicer


class FlightBaseService(FlightServicer):

    def GetFlight(self, request, context):
        return FlightResponse(flight_data=f"Pong: {request}")
