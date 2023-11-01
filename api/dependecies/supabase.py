from starlette.requests import Request
from supabase import Client

def get_supabase_client(request: Request) -> Client:
    return request.app.state.supabase_client
