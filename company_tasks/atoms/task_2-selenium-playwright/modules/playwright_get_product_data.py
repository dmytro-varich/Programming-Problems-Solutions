"""Get product data using Playwright (sync)."""

from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from time import sleep
from typing import Any

from load_django import *  # noqa: F403
from parser_app.models import Product
from playwright.sync_api import Browser, Page, TimeoutError, sync_playwright
from utils.playwright_utils import (
    ScraperUtils as su,
)
from utils.processing_utils import (
    DataProcessingUtils as dpu,
)


def launch_browser() -> tuple[Any, Browser, Page]:
    """Launch browser using Playwright."""
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        channel="chrome",
        headless=False,
        args=["--disable-blink-features=AutomationControlled"],
    )
    context = browser.new_context()
    page = context.new_page()

    print("Create browser")
    return playwright, browser, page


def quit_browser(playwright: Any, browser: Browser) -> None:
    """Close browser."""
    print("QUIT browser")
    browser.close()
    playwright.stop()


def get_url(page: Page, url: str) -> None:
    """Open URL."""
    page.goto(url)
    print("Open link")
    page.wait_for_load_state("domcontentloaded")
    sleep(2)


def search_products(page: Page, product_name: str, *, timeout: int = 10000) -> list:
    """Search products and return locators."""
    try:
        search_input = page.locator("input.quick-search-input:visible").first
        search_input.wait_for(timeout=timeout)
        search_input.fill(product_name)
        search_input.press("Enter")
    except TimeoutError:
        print("Error: Search input not found.")
        return []

    try:
        page.wait_for_selector(".product-wrapper", timeout=timeout)
        products = page.locator(".product-wrapper")
        count = products.count()
        print(f"Found {count} products.")
        return products
    except TimeoutError:
        print("Error: Products not found.")
        return []


def open_first_product(page: Page, products: list) -> bool:
    """Open first product from the search results."""
    if not products or products.count() == 0:
        print("No products found.")
        return False

    try:
        first = products.first
        link = first.locator("a").first.get_attribute("href")

        if not link:
            print("Error: No href.")
            return False

        page.goto(link)
        print(f"Navigated to: {link}")
        page.wait_for_load_state("domcontentloaded")

        return True

    except Exception as e:
        print(f"Error while opening product: {e}")
        return False


def parse_product(page: Page, *, timeout: int = 10000) -> dict[str, Any]:
    """Parse product page."""
    product_data = {}

    # LINK
    product_data["link"] = page.url

    # --- TITLE ---
    product_data["title"] = su.get_element_text(page.locator("h1.main-title"), timeout=timeout)         # noqa: E501

    # --- PRODUCT CODE ---
    product_code_locator = su.select_locator(page.locator("span.br-pr-code-val"), first_visible=True)   # noqa: E501
    product_data["product_code"] = su.get_element_text(product_code_locator, timeout=timeout)           # noqa: E501

    # --- REVIEWS COUNT ---
    reviews_count_locator = su.select_locator(page.locator("a.reviews-count span"), first_visible=True)  # noqa: E501
    product_data["reviews_count"] = su.get_element_text(reviews_count_locator, timeout=timeout)          # noqa: E501

    # --- PROMO PRICE ---
    red_price_locator = su.select_locator(page.locator("span.red-price"), first_visible=True)            # noqa: E501
    red_price = su.get_element_text(red_price_locator, timeout=timeout)
    product_data["promo_price"] = dpu.extract_price(red_price) if red_price else None

    # --- ORIGINAL PRICE ---
    old_price = su.get_element_text(page.locator("div.old-price"), timeout=timeout)

    if old_price:
        original_price = dpu.extract_price(old_price)
    else:
        price = su.get_element_text(page.locator("span.price"), timeout=timeout)
        original_price = dpu.extract_price(price) if price else None

    product_data["original_price"] = original_price

    # --- IMAGES ---
    images = su.get_attributes_list(
        parent_locator=page.locator("div.product-block-bottom"),
        child_selector="img",
        attr="src"
    )
    product_data["images"] = images if images else None

    # --- SPECEFICATIONS ---
    specs = {}

    try:
        items = page.locator("div.br-pr-chr-item")
        count = items.count()

        for i in range(count):
            item = items.nth(i)

            block = su.get_element_dict(
                parent=item,
                selector_main_key="h3",
                selector_row="div > div",
                selector_sub_key="span:first-child",
                selector_sub_value="span:last-child",
                make_nested=True,
            )

            if block:
                specs.update(block)
    except TimeoutError:
        specs = {}

    product_data["specifications"] = specs

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
            product_data[model_field] = value

    # Status update
    product_data["status"] = "Done"

    return product_data


def add_product_in_db(data: dict[str, Any], model: Any) -> None:
    """Add product data to the database."""
    def _save():
        model.objects.update_or_create(link=data["link"], defaults=data)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(_save)
        future.result()


if __name__ == "__main__":
    product_model = Product
    playwright, browser, page = launch_browser()
    get_url(page, "https://brain.com.ua/")
    products = search_products(page, "Apple iPhone 15 128GB Black")
    sleep(5)
    if open_first_product(page, products):
        sleep(5)
        parsed = parse_product(page)
        pprint(parsed)
        add_product_in_db(parsed, product_model)
    quit_browser(playwright, browser)

