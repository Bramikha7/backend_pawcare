from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class ContactMessageCreate(BaseModel):
    full_name: Optional[str] = None
    email: str
    city: Optional[str] = None
    phone_num: Optional[str] = None
    subject: str
    message_content: str
    status: Optional[str] = "New"
class ContactMessageUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[str] = None
    city: Optional[str] = None
    phone_num: Optional[str] = None
    subject: Optional[str] = None
    message_content: Optional[str] = None
    status: Optional[str] = None
class ContactMessageResponse(BaseModel):
    contact_id: int
    full_name: Optional[str]
    email: str
    city: Optional[str]
    phone_num: Optional[str]
    subject: str
    message_content: str
    status: str
    received_at:Optional[datetime]=None
class Config:
    from_attributes = True







