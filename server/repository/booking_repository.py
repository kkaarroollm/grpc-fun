from schemas.bookings import BookingCreate, BookingRead, Flight, Hotel
from api.dependencies import FlightClient, HotelClient


class BookingRepository:

    def _get_flight(self, flight: Flight):
        return FlightClient().get_flight(flight=flight)

    def _get_hotel(self, hotel: Hotel):
        return HotelClient().get_hotel(hotel=hotel)

    def build_booking(self, booking: BookingCreate):
        hotel = self._get_hotel(booking.hotel)
        flight = self._get_flight(booking.flight)

        # return BookingRead(
        #     booking_id=booking.booking_id,
        #     hotel=hotel["hotel_data"],
        #     flight=flight["flight_data"]
        # )
        return [hotel, flight]
