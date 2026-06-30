from pydantic import BaseModel, ConfigDict, Field
from typing import List


# =========================
# CLIENT DTO
# =========================

class ClientCreateDTO(BaseModel):
    name: str = Field(min_length=1)


class ClientOutDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


# =========================
# PRODUCT DTO
# =========================

class ProductCreateDTO(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)


class ProductOutDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: float


# =========================
# ORDER DTO
# =========================

class OrderItemDTO(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


class OrderCreateDTO(BaseModel):
    client_id: int
    items: List[OrderItemDTO]


class OrderItemOutDTO(BaseModel):
    product_id: int
    quantity: int
    price: float


class OrderOutDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    client_id: int
    total: float
    items: List[OrderItemOutDTO]


# Backward-compatible aliases for the CRUD layer and tests.
ClientCreate = ClientCreateDTO
ProductCreate = ProductCreateDTO
OrderCreate = OrderCreateDTO
