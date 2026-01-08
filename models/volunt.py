from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.database import Base
class Volunt(Base):
    __tablename__ = "volunteer"
    volunt_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    applied_at = Column(DateTime, default=datetime.utcnow)
    donations = relationship("Donation", back_populates="volunteer")
    case_reports = relationship("CaseReport", back_populates="volunteer")







