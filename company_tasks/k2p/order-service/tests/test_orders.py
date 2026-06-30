import pytest
from pydantic import ValidationError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import crud, schemas
from app.database import Base
from app.main import app


@pytest.fixture
def db(tmp_path):
    engine = create_engine(
        f"sqlite:///{tmp_path}/orders_test.db",
        connect_args={"check_same_thread": False},
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


def test_app_starts_with_expected_routes():
    paths = set(app.openapi()["paths"])

    assert "/clients/" in paths
    assert "/products/" in paths
    assert "/orders/" in paths
    assert "/orders/client/{client_id}" in paths


def test_full_order_flow(db):
    client = crud.create_client(db, schemas.ClientCreateDTO(name="Test Client"))
    product_1 = crud.create_product(db, schemas.ProductCreateDTO(name="Laptop", price=1000))
    product_2 = crud.create_product(db, schemas.ProductCreateDTO(name="Mouse", price=50))

    order = crud.create_order(db, schemas.OrderCreateDTO(
        client_id=client.id,
        items=[
            schemas.OrderItemDTO(product_id=product_1.id, quantity=1),
            schemas.OrderItemDTO(product_id=product_2.id, quantity=2),
        ],
    ))

    assert order["client_id"] == client.id
    assert order["total"] == 1100
    assert len(order["items"]) == 2

    orders = crud.get_orders_by_client(db, client.id)
    assert len(orders) == 1
    assert orders[0]["total"] == 1100


def test_order_without_client_fails(db):
    with pytest.raises(ValueError, match="Client does not exist"):
        crud.create_order(db, schemas.OrderCreateDTO(
            client_id=9999,
            items=[schemas.OrderItemDTO(product_id=1, quantity=1)],
        ))


def test_order_empty_items_fails(db):
    client = crud.create_client(db, schemas.ClientCreateDTO(name="X"))

    with pytest.raises(ValueError, match="at least one item"):
        crud.create_order(db, schemas.OrderCreateDTO(client_id=client.id, items=[]))


def test_order_with_missing_product_does_not_create_empty_order(db):
    client = crud.create_client(db, schemas.ClientCreateDTO(name="Client"))

    with pytest.raises(ValueError, match="Product 9999 does not exist"):
        crud.create_order(db, schemas.OrderCreateDTO(
            client_id=client.id,
            items=[schemas.OrderItemDTO(product_id=9999, quantity=1)],
        ))

    assert crud.get_orders_by_client(db, client.id) == []


def test_product_price_and_item_quantity_must_be_positive():
    with pytest.raises(ValidationError):
        schemas.ProductCreateDTO(name="Bad product", price=0)

    with pytest.raises(ValidationError):
        schemas.OrderItemDTO(product_id=1, quantity=0)
