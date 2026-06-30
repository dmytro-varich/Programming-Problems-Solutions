from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud

from app.schemas import OrderCreateDTO, OrderOutDTO

router = APIRouter()


@router.post("/", response_model=OrderOutDTO)
def create_order(order: OrderCreateDTO, db: Session = Depends(get_db)):
    try:
        return crud.create_order(db, order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/client/{client_id}", response_model=list[OrderOutDTO])
def get_orders_by_client(client_id: int, db: Session = Depends(get_db)):
    return crud.get_orders_by_client(db, client_id)
