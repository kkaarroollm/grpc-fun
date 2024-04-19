from fastapi import APIRouter
from api.routes.bookings import booking_router

api_router = APIRouter()
api_router.include_router(booking_router, prefix="/bookings", tags=["Bookings"])
