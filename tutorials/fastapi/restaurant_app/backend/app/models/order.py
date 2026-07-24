from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    table_number: Mapped[int] = mapped_column(default=5)
    dish_name: Mapped[str]
    status: Mapped[str] = mapped_column(default="Cooking")
