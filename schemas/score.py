from pydantic import BaseModel

class Score(BaseModel):

    profile_url: str
    website: str
    performance: int | None = None
    accessibility: int | None = None
    best_practices: int | None = None
    seo: int | None = None

    class Config:
        from_attributes = True