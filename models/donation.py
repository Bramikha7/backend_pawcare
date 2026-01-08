from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db.database import Base  
class Donation(Base):
    __tablename__ = "donations"
    id = Column(Integer, primary_key=True, index=True)
    volunt_id = Column(
        Integer,
        ForeignKey("volunteer.volunt_id"),
        nullable=False
    )
    amount = Column(Float, nullable=False)
    payment_method = Column(String(50), nullable=False)
    donor_name = Column(String(100))
    donor_email = Column(String(100))
    donated_at = Column(DateTime, default=datetime.utcnow)
    volunteer = relationship("Volunt", back_populates="donations")
    










