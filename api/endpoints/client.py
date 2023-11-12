
from fastapi import APIRouter, Depends, UploadFile, BackgroundTasks
from starlette import status

from services.parse import ParseService
from services.score import ScoreService
from db.repositories.client import ClientRepo
from schemas.client import Client
from api.dependecies.postgres import get_repository


router = APIRouter()

@router.post(
    "/clients/create/from-csv",
    status_code=status.HTTP_200_OK,
)
async def parse_csv(
    file: UploadFile,
    background_tasks: BackgroundTasks,
    parse_service: ParseService = Depends(ParseService),
    score_service: ScoreService = Depends(ScoreService),
    client_repo: ClientRepo = Depends(get_repository(ClientRepo)),
) -> list[Client]:
    clients = parse_service.clean_csv(file.file)
    await client_repo.create_many(clients)
    for cl in clients:
        background_tasks.add_task(score_service.gather_insight, profile_url=cl.profile_url, website=cl.website)
    return clients

