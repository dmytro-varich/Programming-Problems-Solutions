import pytest


@pytest.mark.asyncio
async def test_create_order_success(client):
    response = await client.post("/api/v1/orders", json={"table_number": 5})
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["table_number"] == 5
    assert "dish_name" in data
    assert data["status"] == "Готовится 👨‍🍳"


@pytest.mark.asyncio
async def test_get_orders_list(client):
    await client.post("/api/v1/orders", json={"table_number": 5})
    await client.post("/api/v1/orders", json={"table_number": 2})

    response = await client.get("/api/v1/orders")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
