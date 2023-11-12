from fastapi import Depends
from core.settings import AppSettings, get_app_settings
from api.dependecies.postgres import get_repository
from db.repositories.score import ScoreRepo
import httpx


class ScoreService:

    def __init__(
        self,
        settings: AppSettings = Depends(get_app_settings),
        score_repo: ScoreRepo = Depends(get_repository(ScoreRepo)),
    ):
        self._base_url = f"https://www.googleapis.com/pagespeedonline"
        self._params = {
            "strategy": "mobile",
            "category": [
                "performance",
                "accessibility",
                "best-practices",
                "seo",
                "pwa",
            ],
            "key": settings.google_api_key,
        }
        self.score_repo = score_repo

    async def gather_insight(
        self,
        profile_url: str,
        website: str,
    ):
        if any([
            domain in website for domain in [
                "gmail",
                "googlemail",
                "hotmail",
                "yahoo",
                "outlook",
                "icloud",
            ]
        ]):
            return
        
        if await self.score_repo.by_profile_url(profile_url):
            return
        
        async with self._cli() as cli:
            params = self.params
            params["url"] = website
            resp = await cli.get(
                url="/v5/runPagespeed",
                params=params,
            )
            resp_json = resp.json()
            lighthouseResult = resp_json.get("lighthouseResult")
            score = {
                "profile_url": profile_url,
                "website": website,
                "performance": lighthouseResult.get("categories").get("performance").get("score") if lighthouseResult else None,
                "accessibility": lighthouseResult.get("categories").get("accessibility").get("score") if lighthouseResult else None,
                "best_practices": lighthouseResult.get("categories").get("best-practices").get("score") if lighthouseResult else None,
                "seo": lighthouseResult.get("categories").get("seo").get("score") if lighthouseResult else None,
            }
        
        return await self.score_repo.create(score)
    
    @property
    def params(self):
        return self._params.copy()
    
    def _cli(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(
            base_url=self._base_url,
            timeout=100,
        )
    