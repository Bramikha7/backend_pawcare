from pydantic import BaseModel
from datetime import date, time
from typing import Optional
class UpcomingVaccinationDriveBase(BaseModel):
    title: str
    location: str
    drive_date: date
    drive_time: time
    status: Optional[str] = "Scheduled"
class UpcomingVaccinationDriveUpdate(BaseModel):
    title: Optional[str] = None
    location: Optional[str] = None
    drive_date: Optional[date] = None
    drive_time: Optional[time] = None
    status: Optional[str] = None