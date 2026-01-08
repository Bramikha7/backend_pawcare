from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.volunt import Volunt
from schemas.volunt import VolunteerCreate, VolunteerUpdate, VolunteerLogin, VolunteerResponse
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

@router.get("/", response_model=list[VolunteerResponse])
def get_all_volunteers(db: Session = Depends(get_db)):
    return db.query(Volunt).all()

@router.get("/{volunt_id}", response_model=VolunteerResponse)
def get_volunteer(volunt_id: int, db: Session = Depends(get_db)):
    volunteer = db.query(Volunt).filter(Volunt.volunt_id == volunt_id).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    return volunteer

@router.put("/{volunt_id}", response_model=VolunteerResponse)
def update_volunteer(volunt_id: int, update_data: VolunteerUpdate, db: Session = Depends(get_db)):
    volunteer = db.query(Volunt).filter(Volunt.volunt_id == volunt_id).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    update_dict = update_data.model_dump(exclude_unset=True)
    for field, value in update_dict.items():
        setattr(volunteer, field, value)
    db.commit()
    db.refresh(volunteer)
    return volunteer

@router.delete("/{volunt_id}")
def delete_volunteer(volunt_id: int, db: Session = Depends(get_db)):
    volunteer = db.query(Volunt).filter(Volunt.volunt_id == volunt_id).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    db.delete(volunteer)
    db.commit()
    return {"message": f"Volunteer with id {volunt_id} has been deleted"}







