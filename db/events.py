from fastapi import FastAPI
from core.settings import AppSettings
import supabase

def connect_to_supabase(app: FastAPI, settings: AppSettings) -> None:
    app.state.supabase_client = supabase.create_client(
        settings.supabase_url,
        settings.supabase_anon_key,
    )