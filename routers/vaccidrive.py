from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.vaccidrive import UpcomingVaccinationDrive
from schemas.vaccidrive import UpcomingVaccinationDriveBase, UpcomingVaccinationDriveUpdate
from dependencies import get_db
router = APIRouter(prefix="/vaccination-drives", tags=["Vaccination Drives"])


@router.get("/")
def get_all_drives(db: Session = Depends(get_db)):
    return db.query(UpcomingVaccinationDrive).all()


@router.post("/")
def create_drive(drive: UpcomingVaccinationDriveBase, db: Session = Depends(get_db)):
    db_drive = UpcomingVaccinationDrive(**drive.model_dump())
    db.add(db_drive)
    db.commit()
    db.refresh(db_drive)
    return db_drive


@router.get("/{drive_id}")
def get_drive(drive_id: int, db: Session = Depends(get_db)):
    drive = db.query(UpcomingVaccinationDrive).filter(UpcomingVaccinationDrive.id == drive_id).first()
    if not drive:
        raise HTTPException(status_code=404, detail="Drive not found")
    return drive


@router.put("/{drive_id}")
def update_drive(drive_id: int, drive_update: UpcomingVaccinationDriveUpdate, db: Session = Depends(get_db)):
    drive = db.query(UpcomingVaccinationDrive).filter(UpcomingVaccinationDrive.id == drive_id).first()
    if not drive:
        raise HTTPException(status_code=404, detail="Drive not found")
    for key, value in drive_update.model_dump(exclude_unset=True).items():
        setattr(drive, key, value)
    db.commit()
    db.refresh(drive)
    return drive


@router.delete("/{drive_id}", status_code=204)
def delete_drive(drive_id: int, db: Session = Depends(get_db)):
    drive = db.query(UpcomingVaccinationDrive).filter(UpcomingVaccinationDrive.id == drive_id).first()
    if not drive:
        raise HTTPException(status_code=404, detail="Drive not found")
    db.delete(drive)
    db.commit()
    return







