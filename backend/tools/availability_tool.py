import json, os
from datetime import datetime, timedelta

APPOINTMENT_TYPES = {
    "consultation": 30,
    "followup": 15,
    "physical": 45,
    "specialist": 60,
}

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DOCTOR_SCHEDULE_FILE = os.path.join(DATA_DIR, "doctor_schedule.json")
BOOKINGS_FILE = os.path.join(DATA_DIR, "bookings.json")


def load_json(path):
    """Load and return data from a JSON file if it exists, otherwise return an empty list."""
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)


def save_json(path, data):
    """Save the given data to a JSON file with indentation."""
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def get_booked_slots_for_date(date_str):
    """Retrieve all booked time slots for a specific date from schedule and booking files."""
    doctor_schedule = load_json(DOCTOR_SCHEDULE_FILE)
    bookings = load_json(BOOKINGS_FILE)
    all_booked = []

    for entry in doctor_schedule:
        if entry["date"] == date_str:
            all_booked.extend(entry["booked_slots"])

    for booking in bookings:
        if booking["date"] == date_str:
            all_booked.append(
                {"start_time": booking["start_time"], "end_time": booking["end_time"]}
            )
    return all_booked


def generate_slots_for_date(date_str, appointment_type):
    """Generate available time slots for a given date and appointment type based on existing bookings."""
    start_of_day = datetime.strptime(f"{date_str} 09:00", "%Y-%m-%d %H:%M")
    end_of_day = datetime.strptime(f"{date_str} 17:00", "%Y-%m-%d %H:%M")
    duration = timedelta(minutes=APPOINTMENT_TYPES[appointment_type])
    booked_slots = get_booked_slots_for_date(date_str)

    slots = []
    current = start_of_day
    while current + duration <= end_of_day:
        start_time = current.strftime("%H:%M")
        end_time = (current + duration).strftime("%H:%M")

        overlap = any(
            (start_time < b["end_time"] and end_time > b["start_time"])
            for b in booked_slots
        )

        slots.append(
            {"start_time": start_time, "end_time": end_time, "available": not overlap}
        )

        current += duration

    return slots
