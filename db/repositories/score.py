from schemas.score import Score as ScoreSchema
from db.models.score import Score
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class ScoreRepo:

    model_class = Score

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, score_attr: dict) -> ScoreSchema:
        model = self.model_class(**score_attr)
        self._session.add(model)
        await self._session.commit()
        await self._session.refresh(model)
        return model

    async def by_profile_url(self, profile_url: str) -> ScoreSchema:
        stmt = select(self.model_class).where(self.model_class.profile_url == profile_url)
        query_result = await self._session.execute(stmt)
        return query_result.first()
