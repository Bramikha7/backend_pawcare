from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class NGOPartnerCreate(BaseModel):
    ngo_name: str
    phone_number: str
    email: EmailStr
    password: str
    city: Optional[str] = None
    service_area: Optional[str] = None
    about_ngo: Optional[str] = None

class NGOPartnerUpdate(BaseModel):
    ngo_name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None
    city: Optional[str] = None
    service_area: Optional[str] = None
    about_ngo: Optional[str] = None

class NGOPartnerLogin(BaseModel):
    email: EmailStr
    password: str

class NGOPartnerResponse(BaseModel):
    ngo_id: int
    registration_no: int
    ngo_name: str
    phone_number: str
    email: EmailStr
    city: Optional[str]
    service_area: Optional[str]
    about_ngo: Optional[str]
    created_at: datetime
    class Config:
        from_attributes = True







