
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
class DonationCreate(BaseModel):
    amount: float
    payment_method: str
    donor_name: Optional[str] = None
    donor_email: Optional[str] = None
class DonationResponse(BaseModel):
    id: int
    volunt_id: int
    amount: float
    payment_method: str
    donor_name: Optional[str]
    donor_email: Optional[str]
    donated_at: datetime
    class Config:
        from_attributes = True  







