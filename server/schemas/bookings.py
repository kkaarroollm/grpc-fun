from uuid import UUID, uuid4

from enum import Enum
from pydantic import BaseModel, field_validator


class FlightClass(str, Enum):
    economy: str = "economy"
    business: str = "business"
    first: str = "first"


class FlightFood(str, Enum):
    vegan: str = "vegan"
    vegetarian: str = "vegetarian"
    gluten_free: str = "gluten_free"
    halal: str = "halal"
    standard: str = "standard"


class FlightLuggage(BaseModel):
    checked: bool
    quantity: int

    @classmethod
    @field_validator("quantity")
    def check_quantity(cls, v, values):
        if not values.get("checked"):
            if v > 0:
                raise ValueError("Quantity must be greater than 0")
        else:
            if v != 0:
                raise ValueError("You don't have any checked luggage")
        return v


class Flight(BaseModel):
    class_: FlightClass
    food: FlightFood
    luggage: FlightLuggage


class Hotel(BaseModel):
    stars: int
    all_inclusive: bool
    room_service: bool
    airport_shuttle: bool


class BookingCreate(BaseModel):
    booking_id: UUID = uuid4()
    flight: Flight
    hotel: Hotel


class BookingRead(BaseModel):
    booking_id: UUID = uuid4()
    flight: Flight
    hotel: Hotel


