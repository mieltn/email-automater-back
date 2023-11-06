from schemas.client import Client as ClientSchema
from db.models.client import Client
from sqlalchemy.ext.asyncio import AsyncSession


class ClientRepo:

    model_class = Client

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_many(self, clients: list[ClientSchema]) -> None:
        models = [self.model_class(**cl.model_dump()) for cl in clients]
        self._session.add_all(models)
        await self._session.commit()

        #     (
        #         self._supabase_client
        #         .table("prospects")
        #         .upsert(cl.model_dump())
        #         .execute()
        #     )
