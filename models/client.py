from pydantic import BaseModel, EmailStr


class Client(BaseModel):

    profile_url: str
    email: EmailStr
    full_name: str
    location: str

    headline: str | None = None
    current_company: str | None = None
    contacted: bool = False
