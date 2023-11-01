from fastapi import Depends
from supabase import Client as SupabaseClient
from models.client import Client
from api.dependecies.supabase import get_supabase_client


class ClientRepo:
    def __init__(
        self,
        supabase_client: SupabaseClient = Depends(get_supabase_client)
    ):
        self._supabase_client = supabase_client

    def create_many(self, clients: list[Client]):
        for cl in clients:
            (
                self._supabase_client
                .table("prospects")
                .upsert(cl.to_dict())
                .execute()
            )
