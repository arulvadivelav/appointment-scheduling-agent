from fastapi import FastAPI
from api import calendly_integration

app = FastAPI(title="Mock Calendly Scheduling API", version="1.0")
app.include_router(calendly_integration.router)


@app.get("/")
def root():
    return {"message": "Calendly mock API is running"}
