from pydantic import BaseModel

class PageAnalytics(BaseModel):

    client_id: int
    website: str | None = None
    accessibility: int | None = None
    best_practices: int | None = None
    seo: int | None = None
    performance: int | None = None