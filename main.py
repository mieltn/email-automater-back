from fastapi import FastAPI
# from fastapi.exceptions import RequestValidationError
# from starlette.exceptions import HTTPException

from core.events import create_start_app_handler
from core.settings import get_app_settings
from api.endpoints.client import router


def get_application() -> FastAPI:

    settings = get_app_settings()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_event_handler(
        "startup",
        create_start_app_handler(application, settings),
    )
    # application.add_event_handler(
    #     "shutdown",
    #     create_stop_app_handler,
    # )

    # application.add_exception_handler(HTTPException, http_error_handler)
    # application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(router, prefix=settings.api_prefix)

    return application

app = get_application()
