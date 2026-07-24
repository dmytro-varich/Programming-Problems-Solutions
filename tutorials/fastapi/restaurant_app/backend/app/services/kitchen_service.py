import random


class KitchenService:
    SPECIAL_DISHES = [
        "Spaghetti Carbonara",
        "Beef Wellington",
        "Chicken Tikka Masala",
        "American Burger",
        "Sushi Platter",
        "Vegan Buddha Bowl",
    ]

    @classmethod
    def get_special_dish(cls) -> str:
        return random.choice(cls.SPECIAL_DISHES)


kitchen_service = KitchenService()
