from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.order import Order


class CRUDOrder:
    async def get_multi(self, db: AsyncSession) -> list[Order]:
        result = await db.execute(select(Order).order_by(Order.id.desc()))
        return list(result.scalars().all())

    async def create(self, db: AsyncSession, dish_name: str, table_number: int) -> Order:
        new_order = Order(dish_name=dish_name, table_number=table_number)
        db.add(new_order)
        await db.commit()
        await db.refresh(new_order)
        return new_order


crud_order = CRUDOrder()
