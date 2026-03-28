"""Parses product details from the provided links and updates the database.

Note:
    I decided not to use AttributeError exception handling, but instead to
    check for None explicitly. This approach keeps the code cleaner and more compact.
"""

from pprint import pprint

import requests
from bs4 import BeautifulSoup
from load_django import *  # noqa: F403
from parser_app.models import Product
from processing_utils import DataProcessingUtils as dpu

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",  # noqa: E501
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",  # noqa: E501
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",  # Do Not Track
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "Trailers",  # Transfer Encoding
}

product = {}

products = Product.objects.all()
for item in products:
    # Fetch page content
    r = requests.get(item.link, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    # Extract data
    # --- TITILE ---
    title_tag = soup.find("h1", attrs={"class": "main-title"}).text.strip()
    product["title"] = dpu.clean_text(title_tag) if title_tag else None

    # --- PRODUCT CODE ---
    product_code = soup.find("span", attrs={"class": "br-pr-code-val"}).text.strip()
    product["product_code"] = dpu.clean_text(product_code) if product_code else None

    # --- REVIEWS COUNT ---
    reviews_link = soup.find("a", attrs={"class": "reviews-count"})
    reviews_count = reviews_link.find("span").text.strip()
    product["reviews_count"] = dpu.clean_text(reviews_count) if reviews_count else None

    # --- PROMO PRICE ---
    red_price_tag = soup.find("span", attrs={"class": "red-price"})
    product["promo_price"] = dpu.extract_price(red_price_tag.get_text()) if red_price_tag else None  # noqa: E501

    # --- ORIGINAL PRICE ---
    old_price_div = soup.find("div", attrs={"class": "old-price"})
    if old_price_div:
        product["original_price"] = dpu.extract_price(old_price_div.get_text())
    else:
        price_tag = soup.find("span", attrs={"class": "price"})
        product["original_price"] = (dpu.extract_price(price_tag.get_text()) if price_tag else None)  # noqa: E501

    # --- IMAGES ---
    img_block = soup.find("div", attrs={"class": "product-block-bottom"})
    if img_block:
        images = [img.get("src") for img in img_block.find_all("img") if img.get("src")]
        product["images"] = images if images else None
    else:
        product["images"] = None

    # --- SPECEFICATIONS ---
    specs = {}
    specs_block = soup.find("div", attrs={"class": "br-pr-chr"})
    if specs_block:
        for spec_item in specs_block.find_all("div", class_="br-pr-chr-item"):
            h3 = spec_item.find("h3")
            spec_key = dpu.clean_text(h3.text.strip()) if h3 else None
            specs.update({spec_key: {}}) if spec_key else None
            for row in (r for c in spec_item.find_all("div", recursive=False)
                          for r in c.find_all("div", recursive=False)):
                spans = row.find_all("span", recursive=False)
                if len(spans) >= 2:
                    key, value = (
                        dpu.clean_text(s.get_text(strip=True)) for s in spans[:2]
                    )
                    if spec_key:
                        specs[spec_key].update({key: value})
                    else:
                        specs.update({key: value})

    product["specifications"] = specs if specs else None

    # --- CURRENT SPECS ---
    specs_mapping = {
        "Колір": "color",
        "Виробник": "vendor",
        "Вбудована пам'ять": "memory",
        "Діагональ екрану": "screen_diagonal",
        "Роздільна здатність екрану": "screen_resolution",
    }

    def find_in_specs(specs, key):
        """Recursively searches for a key in a nested specifications dictionary."""
        if isinstance(specs, dict):
            for k, v in specs.items():
                if k == key:
                    return v
                if isinstance(v, dict):
                    found = find_in_specs(v, key)
                    if found is not None:
                        return found
        return None

    for spec_key, model_field in specs_mapping.items():
        value = find_in_specs(specs, spec_key)
        if value is not None:
            product[model_field] = value

    # Status update
    product["status"] = "Done"

    # Print
    pprint(product)

    # Save to DB
    # for k, v in product.items():
    #     setattr(item, k, v)
    # item.save()

    # Alternative way to update or create the product in the database
    products.update_or_create(link=item.link, defaults=product)

    print("Product updated in DB")
