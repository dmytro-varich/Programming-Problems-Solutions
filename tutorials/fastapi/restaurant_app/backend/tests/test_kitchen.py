from app.services.kitchen_service import kitchen_service

def test_kitchen_returns_valid_dish():
    dish = kitchen_service.get_random_dish()
    assert isinstance(dish, str)
    assert dish in kitchen_service.SPECIAL_DISHES