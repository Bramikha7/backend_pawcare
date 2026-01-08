from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.database import Base
class CaseReport(Base):
    __tablename__ = "case_reports"
    case_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    volunt_id = Column(Integer, ForeignKey("volunteer.volunt_id"), nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    address = Column(Text, nullable=False)
    city = Column(String, nullable=False)
    pincode = Column(String, nullable=False)
    number_of_dogs = Column(Integer, nullable=False)
    urgency_level = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    best_time_to_visit = Column(String, nullable=True)
    status = Column(String, default="Submitted")
    reported_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )
    volunteer = relationship("Volunt", back_populates="case_reports")