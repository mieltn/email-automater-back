from typing import Callable

from fastapi import FastAPI

from core.settings import AppSettings
from db.events import connect_to_supabase


def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:
    def start_app() -> None:
        connect_to_supabase(app, settings)

    return start_app


# def create_stop_app_handler(app: FastAPI) -> Callable:
#     async def stop_app() -> None:
#         await close_db_connection(app)

#     return stop_app
