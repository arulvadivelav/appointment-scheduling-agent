from fastapi import APIRouter, HTTPException, Query
from datetime import date
from tools.availability_tool import generate_slots_for_date, APPOINTMENT_TYPES
from tools.booking_tool import create_booking
from models.schemas import BookingRequest, BookingResponse, AvailabilityResponse

router = APIRouter(prefix="/api/calendly", tags=["Calendly Mock"])


@router.get("/availability", response_model=AvailabilityResponse)
def get_availability(date: date = Query(...), appointment_type: str = Query(...)):
    """Fetch available appointment slots for a specific date and appointment type."""
    if appointment_type not in APPOINTMENT_TYPES:
        raise HTTPException(status_code=400, detail="Invalid appointment type")
    slots = generate_slots_for_date(str(date), appointment_type)
    return {
        "date": date,
        "appointment_type": appointment_type,
        "available_slots": slots,
    }


@router.post("/book", response_model=BookingResponse)
def book_appoincreate_bookingtment(booking_req: BookingRequest):
    """Create a new appointment booking for the requested date and slot."""
    result = create_booking(booking_req)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result)
    return {
        "booking_id": result["booking_id"],
        "status": result["status"],
        "confirmation_code": result["confirmation_code"],
        "details": result,
    }
