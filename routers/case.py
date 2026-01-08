from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.volunt import Volunt
from models.case import CaseReport
from schemas.case import CaseReportCreate, CaseReportUpdate, CaseReportResponse
from dependencies import get_db
router = APIRouter(prefix="/case-reports", tags=["Case Reports"])
@router.post("/", response_model=CaseReportResponse)
def create_case_report(
    case: CaseReportCreate,
    volunt_id: int,
    db: Session = Depends(get_db)
):
   
    volunteer = db.query(Volunt).filter(
        Volunt.volunt_id == volunt_id
    ).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    new_case = CaseReport(
        volunt_id=volunt_id,
        **case.model_dump()
    )
    db.add(new_case)
    db.commit()
    db.refresh(new_case)
    return new_case
@router.get("/", response_model=list[CaseReportResponse])
def get_all_case_reports(db: Session = Depends(get_db)):
    return db.query(CaseReport).all()
@router.get("/{case_id}", response_model=CaseReportResponse)
def get_case_report(case_id: int, db: Session = Depends(get_db)):
    report = db.query(CaseReport).filter(CaseReport.case_id == case_id).first()
    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Case report not found"
        )
    return report
@router.put("/{case_id}", response_model=CaseReportResponse)
def update_case_report(
    case_id: int,
    case_update: CaseReportUpdate,
    db: Session = Depends(get_db)
):
    report = db.query(CaseReport).filter(CaseReport.case_id == case_id).first()
    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Case report not found"
        )
    update_data = case_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        if value is not None:
            setattr(report, key, value)
    db.commit()
    db.refresh(report)
    return report




















