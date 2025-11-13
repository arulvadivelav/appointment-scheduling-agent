import json, os, uuid, random, string
from .availability_tool import (
    APPOINTMENT_TYPES,
    generate_slots_for_date,
    save_json,
    BOOKINGS_FILE,
)
from datetime import datetime, timedelta


def is_slot_available(date_str, appointment_type, start_time):
    """Check if a specific appointment slot is available for the given date and type."""
    slots = generate_slots_for_date(date_str, appointment_type)
    start_time = datetime.strptime(start_time, "%H:%M").strftime("%H:%M")
    for slot in slots:
        if slot["start_time"] == start_time:
            return slot["available"]
    return False


def create_booking(booking_req):
    """Create and save a booking if the requested slot is available, otherwise suggest alternate slots."""
    if not is_slot_available(
        str(booking_req.date), booking_req.appointment_type, booking_req.start_time
    ):
        alt_slots = [
            s
            for s in generate_slots_for_date(
                str(booking_req.date), booking_req.appointment_type
            )
            if s["available"]
        ]
        return {
            "error": "Requested slot not available",
            "suggested_slots": alt_slots[:3],
        }

    booking_id = f"APPT-{uuid.uuid4().hex[:8].upper()}"
    confirmation_code = "".join(
        random.choices(string.ascii_uppercase + string.digits, k=6)
    )
    duration = APPOINTMENT_TYPES[booking_req.appointment_type]

    start_hour, start_min = map(int, booking_req.start_time.split(":"))
    start_dt = datetime.strptime(f"{start_hour:02d}:{start_min:02d}", "%H:%M")
    end_dt = start_dt + timedelta(minutes=duration)
    end_time = end_dt.strftime("%H:%M")

    booking_entry = {
        "booking_id": booking_id,
        "status": "confirmed",
        "confirmation_code": confirmation_code,
        "appointment_type": booking_req.appointment_type,
        "date": str(booking_req.date),
        "start_time": booking_req.start_time,
        "end_time": end_time,
        "patient": booking_req.patient.dict(),
        "reason": booking_req.reason,
    }

    bookings = []
    if os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, "r") as f:
            bookings = json.load(f)
    bookings.append(booking_entry)
    save_json(BOOKINGS_FILE, bookings)
    return booking_entry
