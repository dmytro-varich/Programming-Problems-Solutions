"""Seeds the database with product links for parsing."""

from load_django import *  # noqa: F403
from parser_app.models import Product

url = "https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html"  # noqa: E501


Product.objects.get_or_create(link=url)
