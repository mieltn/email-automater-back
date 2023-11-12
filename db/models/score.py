from sqlalchemy import Column, String, Float
from db.sessions import Base

class Score(Base):

    __tablename__ = "scores"

    profile_url = Column(String, primary_key=True)
    website = Column(String, nullable=True)
    accessibility = Column(Float, nullable=True)
    best_practices = Column(Float, nullable=True)
    seo = Column(Float, nullable=True)
    performance = Column(Float, nullable=True)
    