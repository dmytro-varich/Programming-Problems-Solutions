from pydantic import BaseModel

class OrderCreate(BaseModel):
    table_number: int = 5

class OrderResponse(BaseModel):
    id: int
    table_number: int
    dish_name: str
    status: str

    class Config:
        from_attributes = True