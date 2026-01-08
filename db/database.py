from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE
DB_URL = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
engine = create_engine(DB_URL)
Sessionlocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()