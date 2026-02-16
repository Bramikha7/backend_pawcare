from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from dependencies import get_db
from sqlalchemy import func
from models.volunt import Volunt
from schemas.volunt import VolunteerCreate, VolunteerLogin, VolunteerResponse,VolunteerCountResponse
router = APIRouter(prefix="/volunteers", tags=["Volunteers"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=VolunteerResponse)
def create_volunteer(volunteer: VolunteerCreate, db: Session = Depends(get_db)):

    if db.query(Volunt).filter(Volunt.email == volunteer.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    new_volunteer = Volunt(
        name=volunteer.name,
        phone_number=volunteer.phone_number,
        email=volunteer.email,
        password=volunteer.password
    )
    db.add(new_volunteer)
    db.commit()
    db.refresh(new_volunteer)
    return new_volunteer

@router.post("/signin")
def volunteer_signin(credentials: VolunteerLogin, db: Session = Depends(get_db)):
    volunteer = db.query(Volunt).filter(Volunt.email == credentials.email).first()
    if not volunteer or volunteer.password != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Signed in successfully", "volunt_id": volunteer.volunt_id}

@router.get("/count",response_model=VolunteerCountResponse)
def get_volunteer_count(db:Session=Depends(get_db)):
    total_volunteers=db.query(func.count(Volunt.volunt_id)).scalar()
    return{"total_volunteers":total_volunteers}

@router.get("/", response_model=list[VolunteerResponse])
def get_all_volunteers(db: Session = Depends(get_db)):
    return db.query(Volunt).all()

@router.get("/{volunt_id}", response_model=VolunteerResponse)
def get_volunteer(volunt_id: int, db: Session = Depends(get_db)):
    volunteer = db.query(Volunt).filter(Volunt.volunt_id == volunt_id).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    return volunteer

@router.delete("/{volunt_id}")
def delete_volunteer(volunt_id: int, db: Session = Depends(get_db)):
    volunteer = db.query(Volunt).filter(Volunt.volunt_id == volunt_id).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    db.delete(volunteer)
    db.commit()
    return {"message": f"Volunteer with id {volunt_id} has been deleted"}







