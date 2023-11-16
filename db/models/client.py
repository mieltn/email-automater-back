from sqlalchemy import Column, Integer, String, Boolean
from db.sessions import Base

class Client(Base):

    __tablename__ = "linkedin_prospects"

    id = Column(Integer, primary_key=True)
    profile_url = Column(String, unique=True)
    email = Column(String)
    website = Column(String)
    full_name = Column(String)
    location = Column(String)
    headline = Column(String, nullable=True)
    current_company = Column(String, nullable=True)
    contacted: bool = Column(Boolean, nullable=True)
