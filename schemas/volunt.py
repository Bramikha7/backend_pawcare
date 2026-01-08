from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class VolunteerCreate(BaseModel):
    name: str
    phone_number: Optional[str] = None
    email: EmailStr
    password: str

class VolunteerUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class VolunteerLogin(BaseModel):
    email: EmailStr
    password: str

class VolunteerResponse(BaseModel):
    volunt_id: int
    name: str
    phone_number: Optional[str] = None
    email: EmailStr
    applied_at: Optional[datetime] = None
    class Config:
        from_attributes = True







