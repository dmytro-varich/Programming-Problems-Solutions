from sqlalchemy.orm import Session
from app import models, schemas


# -------------------
# CLIENT
# -------------------

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(name=client.name)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def get_clients(db: Session):
    return db.query(models.Client).all()


# -------------------
# PRODUCT
# -------------------

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        price=product.price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session):
    return db.query(models.Product).all()


# -------------------
# ORDER
# -------------------

def create_order(db: Session, order_data: schemas.OrderCreate):
    client = db.query(models.Client).filter(models.Client.id == order_data.client_id).first()
    if not client:
        raise ValueError("Client does not exist")

    if not order_data.items:
        raise ValueError("Order must contain at least one item")

    order = models.Order(client_id=order_data.client_id)

    try:
        db.add(order)
        db.flush()

        for item in order_data.items:
            product = db.query(models.Product).filter(models.Product.id == item.product_id).first()

            if not product:
                raise ValueError(f"Product {item.product_id} does not exist")

            db.add(models.OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=item.quantity
            ))

        db.commit()
        db.refresh(order)
        return serialize_order(order)
    except ValueError:
        db.rollback()
        raise


def get_orders_by_client(db: Session, client_id: int):
    orders = db.query(models.Order).filter(models.Order.client_id == client_id).all()
    return [serialize_order(order) for order in orders]


def serialize_order(order: models.Order):
    items = [
        {
            "product_id": item.product_id,
            "quantity": item.quantity,
            "price": item.product.price,
        }
        for item in order.items
    ]

    return {
        "id": order.id,
        "client_id": order.client_id,
        "total": sum(item["price"] * item["quantity"] for item in items),
        "items": items,
    }
