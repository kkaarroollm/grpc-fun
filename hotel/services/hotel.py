from pb.hotel_pb2 import HotelResponse
from pb.hotel_pb2_grpc import HotelServicer


class HotelBaseService(HotelServicer):
    def GetHotel(self, request, context):
        return HotelResponse(hotel_data=f"Pong {request}")
