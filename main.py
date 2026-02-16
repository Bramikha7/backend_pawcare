from fastapi import FastAPI
from db.database import engine,Base
from  fastapi.middleware.cors import CORSMiddleware
from routers import volunt, ngo, vaccidrive, contact, case, donation
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)
@app.get("/")
def read_root():
    return {"message": "Welcome to the PawCare API", "docs": "/docs"}
    
app.include_router(volunt.router)
app.include_router(ngo.router)
app.include_router(vaccidrive.router)
app.include_router(contact.router)
app.include_router(case.router)
app.include_router(donation.router)
