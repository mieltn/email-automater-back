from sqlalchemy import Column, Integer, String
from db.sessions import Base

class Client(Base):

    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    profile_url = Column(String, nullable=False)
    email = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    headline = Column(String, nullable=True)
    current_company = Column(String, nullable=True)
    contacted: bool = Column(String, nullable=True)
