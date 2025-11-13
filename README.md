# Calendly Integration (Mock Scheduling API)

## Overview
This project is a mock scheduling API built with **FastAPI** that simulates Calendly-style meeting booking and management.  
It provides endpoints to book meetings and check availability

## Features
- Create and fetch meeting schedules.
- Check available meeting slots.

## Tech Stack
- **Backend Framework:** FastAPI  
- **Database:** Mocked JSON file
- **Language:** Python 3.9+  
- **API Documentation:** Swagger UI and ReDoc

---

## Folder Structure
```
appointment-scheduling-agent/
│
├── backend/
│   ├── api/
│   │   └── calendly_integration.py
│   │
│   ├── data/
│   │   ├── bookings.json
│   │   └── doctor_schedule.json
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── tools/
│   │   ├── availability_tool.py
│   │   ├── booking_tool.py
│   │
│   ├── main.py
│   ├── requirements.txt
│
├── venv/
│
├── README.md
└── requirements.txt
```

---

## Setup Instructions

### 1. Clone the Repository

```
cd appointment-scheduling-agent/backend
```
1. Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Run the FastAPI App
```
uvicorn main:app --reload
```

## API Documentation
Once the server is running, open:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
