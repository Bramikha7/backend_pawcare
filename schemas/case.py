from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class CaseReportCreate(BaseModel):
    name: str
    phone: str
    email: EmailStr
    address: str
    city: str
    pincode: str
    number_of_dogs: int
    urgency_level: str
    description: Optional[str] = None
    best_time_to_visit: Optional[str] = None

class CaseReportUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    city: Optional[str] = None
    pincode: Optional[str] = None
    number_of_dogs: Optional[int] = None
    urgency_level: Optional[str] = None
    description: Optional[str] = None
    best_time_to_visit: Optional[str] = None
    status: Optional[str] = None

class CaseReportResponse(BaseModel):
    case_id: int
    volunt_id: int
    name: str
    phone: str
    email: str
    address: str
    city: str
    pincode: str
    number_of_dogs: int
    urgency_level: str
    description: Optional[str] = None
    best_time_to_visit: Optional[str] = None
    status: str
    reported_at: datetime
    model_config = {"from_attributes": True}







