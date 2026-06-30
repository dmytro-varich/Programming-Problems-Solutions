from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud

from app.schemas import ProductCreateDTO, ProductOutDTO

router = APIRouter()


@router.post("/", response_model=ProductOutDTO)
def create_product(product: ProductCreateDTO, db: Session = Depends(get_db)):
    return crud.create_product(db, product)


@router.get("/", response_model=list[ProductOutDTO])
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)
