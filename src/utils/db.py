from sqlalchemy import create_engine  #create_engine= creates DB Connection
from sqlalchemy.orm import sessionmaker,declarative_base  #sessions- create DB session and declarative_base= base class fro models
from src.utils.settings import settings  #contains config like DB URL
Base=declarative_base()  #parent class for all ORM MODels
engine=create_engine(url=settings.DB_CONNECTION)  #establiishes connection to your DB

LocalSession=sessionmaker(bind=engine) #creates session objects
#A transactional workspace to query/update DB

#Dependency Injection

# Creates a new DB session per request
# Yields it to your API endpoint
# Ensures it is closed after request finishes
def get_db():
    session=LocalSession()
    try:
        yield session
    finally:
        session.close()