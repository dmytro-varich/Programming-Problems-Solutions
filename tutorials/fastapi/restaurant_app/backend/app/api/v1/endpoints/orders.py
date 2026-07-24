from fastapi import APIRouter, Depends, HTTPException
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
    dish = await kitchen_service.get_dish_by_name(order.dish_name)
    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    return await crud_order.create(
        db,
        dish_name=order.dish_name,
        table_number=order.table_number
    )
