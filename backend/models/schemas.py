from pydantic import BaseModel, EmailStr
from typing import List
from datetime import date


class Slot(BaseModel):
    start_time: str
    end_time: str
    available: bool


class AvailabilityResponse(BaseModel):
    date: date
    appointment_type: str
    available_slots: List[Slot]


class Patient(BaseModel):
    name: str
    email: EmailStr
    phone: str


class BookingRequest(BaseModel):
    appointment_type: str
    date: date
    start_time: str
    patient: Patient
    reason: str


class BookingResponse(BaseModel):
    booking_id: str
    status: str
    confirmation_code: str
    details: dict
