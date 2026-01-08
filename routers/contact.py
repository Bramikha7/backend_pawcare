from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.contact import ContactMessage
from schemas.contact import ContactMessageCreate,ContactMessageResponse
from dependencies import get_db
router = APIRouter(prefix="/contact-messages",tags=["Contact Messages"])


@router.get("/", response_model=list[ContactMessageResponse])
def get_all_messages(db: Session = Depends(get_db)):
    return db.query(ContactMessage).all()


@router.post("/", response_model=ContactMessageResponse)
def create_message(
    message: ContactMessageCreate,
    db: Session = Depends(get_db)
):
    db_message = ContactMessage(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


@router.get("/{contact_id}", response_model=ContactMessageResponse)
def get_message_by_id(contact_id: int, db: Session = Depends(get_db)):
    message = db.query(ContactMessage).filter(
        ContactMessage.contact_id == contact_id
    ).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message










