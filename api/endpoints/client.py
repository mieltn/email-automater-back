
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from starlette import status

from services.parse import ParseService
from db.repositories.client import ClientRepo
from api.dependecies.supabase import get_supabase_client
from models.client import Client


router = APIRouter()

@router.post(
    "/clients/create/from-csv",
    status_code=status.HTTP_200_OK,
)
def parse_csv(
    file: UploadFile,
    parse_service: ParseService = Depends(ParseService),
    client_repo: ClientRepo = Depends(ClientRepo),
) -> list[Client]:
    clients = parse_service.clean_csv(file.file)
    client_repo.create_many(clients)
    return clients

