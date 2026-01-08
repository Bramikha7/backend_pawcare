from db.database import Sessionlocal
def get_db():
    db = Sessionlocal()
    try:
        print("get_db")
        yield db
    finally:
        db.close()







