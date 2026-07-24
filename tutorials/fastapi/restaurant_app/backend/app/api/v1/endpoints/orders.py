from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.schemas.order import OrderCreate, OrderResponse
from app.crud.crud_order import crud_order
from app.services.kitchen_service import kitchen_service


router = APIRouter()


@router.get("", response_model=list[OrderResponse])
async def read_orders(db: AsyncSession = Depends(get_db)):
    return await crud_order.get_multi(db)


@router.post("", response_model=OrderResponse)
async def create_order(
    order: OrderCreate,
    db: AsyncSession = Depends(get_db)
):
    dish_name = kitchen_service.get_special_dish()
    return await crud_order.create(
        db,
        dish_name=dish_name,
        table_number=order.table_number
    )
