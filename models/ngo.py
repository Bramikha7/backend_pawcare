from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from db.database import Base
from datetime import datetime
class NGOPartner(Base):
    __tablename__ = "ngo_partners"
   
    ngo_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
   
    registration_no = Column(Integer, unique=True, index=True, nullable=False)
    ngo_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    city = Column(String, nullable=True)
    service_area = Column(Text, nullable=True)
    about_ngo = Column(Text, nullable=True)
    registration_proof = Column(String, nullable=True)
    created_at = Column(
        TIMESTAMP(timezone=True),
        default=datetime.utcnow
    )







