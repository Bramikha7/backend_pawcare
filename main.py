from fastapi import FastAPI
from db.database import engine,Base
from routers import volunt, ngo, vaccidrive, contact, case, donation
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to the PawCare API!", "docs": "/docs"}
@app.on_event("startup")
def startup():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("Warning: could not create DB tables:", e)
app.include_router(volunt.router)
app.include_router(ngo.router)
app.include_router(vaccidrive.router)
app.include_router(contact.router)
app.include_router(case.router)
app.include_router(donation.router)
