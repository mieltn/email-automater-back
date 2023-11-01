from functools import lru_cache
from pydantic import PostgresDsn, SecretStr, Field
from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):

    debug: bool = False
    docs_url: str = "/docs"
    title: str = "Email Automator API"
    version: str = "0.0.0"

    # database_url: PostgresDsn
    # max_connection_count: int = 10
    # min_connection_count: int = 10
    google_api_key: str
    supabase_url: str
    supabase_anon_key: str

    # secret_key: SecretStr

    api_prefix: str = "/v1"

    allowed_hosts: list[str] = ["*"]

    @property
    def fastapi_kwargs(self) -> dict:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "title": self.title,
            "version": self.version,
        }
    
    class Config:
        env_file = ".env"
    

@lru_cache
def get_app_settings() -> AppSettings:
    return AppSettings()