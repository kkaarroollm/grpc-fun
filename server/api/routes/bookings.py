from fastapi import APIRouter, Depends

from schemas.bookings import BookingCreate, BookingRead
from repository import BookingRepository

booking_router = APIRouter()


@booking_router.post("", name="book_flight")
def book_flight(
        booking: BookingCreate,
        repo: BookingRepository = Depends(BookingRepository)
):
    return repo.build_booking(booking)
