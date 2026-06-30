from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud

from app.schemas import ClientCreateDTO, ClientOutDTO

router = APIRouter()


@router.post("/", response_model=ClientOutDTO)
def create_client(client: ClientCreateDTO, db: Session = Depends(get_db)):
    return crud.create_client(db, client)


@router.get("/", response_model=list[ClientOutDTO])
def get_clients(db: Session = Depends(get_db)):
    return crud.get_clients(db)
