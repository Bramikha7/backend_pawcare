from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.volunt import Volunt
from models.donation import Donation
from schemas.donation import DonationCreate, DonationResponse
from dependencies import get_db
router = APIRouter(prefix="/donations", tags=["Donations"])
@router.post(
    "/volunteers/{volunt_id}/donations",
    response_model=DonationResponse,
    status_code=status.HTTP_201_CREATED
)
def create_donation(
    volunt_id: int,
    donation: DonationCreate,
    db: Session = Depends(get_db)
):
   
    volunteer = db.query(Volunt).filter(Volunt.volunt_id == volunt_id).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    new_donation = Donation(
        volunt_id=volunt_id,
        amount=donation.amount,
        payment_method=donation.payment_method,
        donor_name=donation.donor_name,
        donor_email=donation.donor_email,
    )
    db.add(new_donation)
    db.commit()
    db.refresh(new_donation)
    return new_donation


@router.get("/", response_model=list[DonationResponse])
def get_all_donations(db: Session = Depends(get_db)):
    return db.query(Donation).all()


@router.get("/{donation_id}", response_model=DonationResponse)
def get_donation_by_id(donation_id: int, db: Session = Depends(get_db)):
    donation = db.query(Donation).filter(Donation.id == donation_id).first()
    if not donation:
        raise HTTPException(status_code=404, detail="Donation not found")
    return donation










