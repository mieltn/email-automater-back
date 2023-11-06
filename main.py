from fastapi import FastAPI
from core.settings import get_app_settings
from api.endpoints.client import router


def get_application() -> FastAPI:

    settings = get_app_settings()

    application = FastAPI(**settings.fastapi_kwargs)

    application.include_router(router, prefix=settings.api_prefix)

    return application

app = get_application()
