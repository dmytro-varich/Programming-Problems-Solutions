"""Get product data using Selenium."""

from pprint import pprint
from time import sleep
from typing import Any

from load_django import *  # noqa: F403
from parser_app.models import Product
from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.processing_utils import (
    DataProcessingUtils as dpu,  # our custom utility functions for data processing
)
from utils.selenium_utils import (
    ScraperUtils as su,  # our custom utility functions for Selenium operations
)
from webdriver_manager.chrome import ChromeDriverManager


def launch_browser() -> webdriver.Chrome:
    """Launch the Chrome browser."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options,
                              service=ChromeService(ChromeDriverManager().install()))
    print("Create driver")
    return driver


def quit_driver(driver: webdriver.Chrome) -> None:
    """Quit the Chrome browser."""
    print("QUIT driver")
    driver.quit()


def get_url(driver: webdriver.Chrome, url: str) -> None:
    """Get the URL in the browser."""
    driver.get(url)
    print("Open link")
    sleep(2)


def search_products(driver: webdriver.Chrome, product_name: str, *, wait: int = 10) -> list:  # noqa: E501
    """Search for products on the site and return the list of product elements."""
    wait = WebDriverWait(driver, wait)

    try:
        # This is an alternative way to find the search input:
        # inputs = driver.find_elements(By.CLASS_NAME, "quick-search-input")
        # visible_input = next((inp for inp in inputs if inp.is_displayed()), None)

        visible_input = wait.until(EC.visibility_of_any_elements_located(
            (By.CSS_SELECTOR, "input.quick-search-input")
        ))[0]

        if not visible_input:
            print("Error: No search input found.")
            return []

        visible_input.clear()
        visible_input.send_keys(product_name)
        visible_input.send_keys(Keys.ENTER)

    except NoSuchElementException:
        print("Error while searching for product: Search input not found.")
        return []

    try:
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrapper"))
        )
        products = driver.find_elements(By.CSS_SELECTOR, ".product-wrapper")
        print(f"Found {len(products)} products.")
        return products
    except TimeoutException:
        print("Error while searching for product: Products not found.")
        return []


def open_first_product(driver: webdriver.Chrome, products: list) -> bool:
    """Open the first product from the search results."""
    if not products:
        print("No products found.")
        return False

    try:
        first_product = products[0]
        product_link = first_product.find_element(By.TAG_NAME, "a")
        href = product_link.get_attribute("href")

        if not href:
            print("Error: Product link does not have href attribute.")
            return False

        driver.get(href)
        print(f"Navigated to product page via href: {href}")

        return True
    except (NoSuchElementException, ElementClickInterceptedException) as e:
        print(f"Error while opening product: {e}")
        return False


def parse_product(driver: webdriver.Chrome, *, wait: int = 10) -> dict[str, Any]:
    """Parse product data from the page."""
    product_data = {}
    wait = WebDriverWait(driver, wait)

    # Link to the product page
    product_data["link"] = driver.current_url

    # --- TITLE ---
    product_data["title"] = su.get_element_text(
        wait, (By.CSS_SELECTOR, "h1.main-title")
    )

    # --- PRODUCT CODE ---
    product_data["product_code"] = su.get_element_text(
        wait, (By.CSS_SELECTOR, "span.br-pr-code-val")
    )

    # --- REVIEWS COUNT ---
    product_data["reviews_count"] = su.get_element_text(
        wait, (By.CSS_SELECTOR, "a.reviews-count span")
    )

    # --- PROMO PRICE ---
    red_price = su.get_element_text(wait, (By.CSS_SELECTOR, "span.red-price"))
    product_data["promo_price"] = dpu.extract_price(red_price) if red_price else None

    # --- ORIGINAL PRICE ---
    old_price = su.get_element_text(wait, (By.CSS_SELECTOR, "div.old-price"))

    if old_price:
        original_price = dpu.extract_price(old_price)
    else:
        price_text = su.get_element_text(wait, (By.CSS_SELECTOR, "span.price"))
        original_price = dpu.extract_price(price_text) if price_text else None

    product_data["original_price"] = original_price

    # --- IMAGES ---
    images = su.get_attributes_list(
        wait,
        parent_locator=(By.CSS_SELECTOR, "div.product-block-bottom"),
        child_locator=(By.TAG_NAME, "img"),
    )
    product_data["images"] = images if images else None

    # --- SPECEFICATIONS ---
    specs = {}
    specs_items = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.br-pr-chr-item"))
    )
    for item in specs_items:
        block = su.get_element_dict(
            parent_element=item,
            locator_main_key=(By.TAG_NAME, "h3"),
            locator_row=(By.XPATH, ".//div[span[2]]"),
            locator_sub_key=(By.XPATH, "./span[1]"),
            locator_sub_value=(By.XPATH, "./span[2]"),
            make_nested=True
        )

        if block:
            specs.update(block)

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
    model.objects.update_or_create(link=data["link"], defaults=data)


if __name__ == "__main__":
    product_model = Product
    driver = launch_browser()
    sleep(1)
    get_url(driver, "https://brain.com.ua/")
    products = search_products(driver, "Apple iPhone 15 128GB Black")
    sleep(10)
    is_open = open_first_product(driver, products)
    if is_open:
        sleep(5)
        parsed_product = parse_product(driver)
        sleep(10)
        pprint(parsed_product)
        add_product_in_db(parsed_product, product_model)
    quit_driver(driver)
