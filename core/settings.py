from functools import lru_cache
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

    postgres_host: str
    postgres_port: int
    postgres_db: str
    postgres_user: str
    postgres_password: str

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
    
    @property
    def sync_postgres_dsn(self) -> str:
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"

    @property
    def async_postgres_dsn(self) -> str:
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
    
    class Config:
        env_file = ".env"
    

@lru_cache
def get_app_settings() -> AppSettings:
    return AppSettings()