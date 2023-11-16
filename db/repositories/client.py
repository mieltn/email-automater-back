from schemas.client import Client as ClientSchema
from db.models.client import Client
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert


class ClientRepo:

    model_class = Client

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_many(self, clients: list[ClientSchema]) -> None:
        models  = [cl.model_dump() for cl in clients]
        await self._session.execute(
            insert(self.model_class)
            .values(models)
            .on_conflict_do_nothing()
        )
        await self._session.commit()
