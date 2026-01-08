from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from db.database import Base
class ContactMessage(Base):
    __tablename__ = "contact_messages"
    contact_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, nullable=False)
    city = Column(String)
    phone_num = Column(String)
    subject = Column(String, nullable=False)
    message_content = Column(Text, nullable=False)
    received_at = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String, default="New")







