from fastapi import Depends
from supabase import Client as SupabaseClient
from models.analytics import PageAnalytics
from api.dependecies.supabase import get_supabase_client


class AnalyticsRepo:
    def __init__(
        self,
        supabase_client: SupabaseClient = Depends(get_supabase_client)
    ):
        self._supabase_client = supabase_client

    def create(self, page_analytics: PageAnalytics):
        return (
            self._supabase_client
            .table("analytics")
            .insert(page_analytics.to_dict())
            .execute()
        )