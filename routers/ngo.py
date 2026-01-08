from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.ngo import NGOPartner
from schemas.ngo import (
    NGOPartnerCreate,
    NGOPartnerUpdate,
    NGOPartnerLogin
)
router = APIRouter(
    prefix="/ngo-partners",
    tags=["NGO Partners"]
)

@router.get("/")
def get_all_ngos(db: Session = Depends(get_db)):
    return db.query(NGOPartner).all()

@router.post("/")
def create_ngo(ngo: NGOPartnerCreate, db: Session = Depends(get_db)):
   
    last_ngo = (
        db.query(NGOPartner)
        .order_by(NGOPartner.registration_no.desc())
        .first()
    )
    if last_ngo:
        new_reg_no = last_ngo.registration_no + 1
    else:
        new_reg_no = 1001 
    new_ngo = NGOPartner(
        ngo_name=ngo.ngo_name,
        registration_no=new_reg_no,
        phone_number=ngo.phone_number,
        email=ngo.email,
        password=ngo.password,
        city=ngo.city,
        service_area=ngo.service_area,
        about_ngo=ngo.about_ngo
    )
    db.add(new_ngo)
    db.commit()
    db.refresh(new_ngo)
    return {
        "message": "NGO registered successfully",
        "ngo_id": new_ngo.ngo_id,
        "registration_no": new_ngo.registration_no
    }

@router.post("/signin")
def ngo_signin(
    credentials: NGOPartnerLogin,
    db: Session = Depends(get_db)
):
    ngo = db.query(NGOPartner).filter(
        NGOPartner.email == credentials.email
    ).first()
    if not ngo or ngo.password != credentials.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    return {
        "message": "Signed in successfully",
        "ngo_id": ngo.ngo_id,
        "registration_no": ngo.registration_no
    }

@router.get("/{ngo_id}")
def get_ngo_by_id(
    ngo_id: int,
    db: Session = Depends(get_db)
):
    ngo = db.query(NGOPartner).filter(
        NGOPartner.ngo_id == ngo_id
    ).first()
    if not ngo:
        raise HTTPException(
            status_code=404,
            detail="NGO not found"
        )
    return ngo

@router.put("/{ngo_id}")
def update_ngo(
    ngo_id: int,
    ngo_data: NGOPartnerUpdate,
    db: Session = Depends(get_db)
):
    ngo = db.query(NGOPartner).filter(
        NGOPartner.ngo_id == ngo_id
    ).first()
    if not ngo:
        raise HTTPException(
            status_code=404,
            detail="NGO not found"
        )
    for key, value in ngo_data.dict(exclude_unset=True).items():
        setattr(ngo, key, value)
    db.commit()
    db.refresh(ngo)
    return {
        "message": "NGO updated successfully",
        "ngo": ngo
    }

@router.delete("/{ngo_id}")
def delete_ngo(
    ngo_id: int,
    db: Session = Depends(get_db)
):
    ngo = db.query(NGOPartner).filter(
        NGOPartner.ngo_id == ngo_id
    ).first()
    if not ngo:
        raise HTTPException(
            status_code=404,
            detail="NGO not found"
        )
    db.delete(ngo)
    db.commit()
    return {
        "message": f"NGO with id {ngo_id} deleted successfully"
    }