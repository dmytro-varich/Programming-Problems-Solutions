# TO DO: 
# You need to create a class that will collect data based on the link to the Ebay product page, 
# the data format in which the json data should be returned in the test task can simply be output to the console or saved to a file. 
# Mandatory data is the name, link to the photo, link to the product itself, price, seller, delivery price. Indeed, the more data, 
# the better, but in the context of the test it is not important.
import requests, json
from bs4 import BeautifulSoup

class eBayProductScraper:
    def __init__(self, url):
        self.product_url = url

    def fetch_product_page(self):
        response = requests.get(self.product_url)
        response.raise_for_status()
        return response.text

    def parse_product_data(self) -> dict | None:
        response = self.fetch_product_page()
        soup = BeautifulSoup(response, "html.parser")
        item_data = {}

        try: 
            # Product Name
            item_title_element = soup.select_one(".x-item-title__mainTitle .ux-textspans--BOLD")
            title = item_title_element.text if item_title_element else "Not available"

            # Price 
            current_price_element = soup.select_one(".x-price-primary .ux-textspans")
            current_price = current_price_element.text if current_price_element else "Not available"

            original_price_element = soup.select_one(".ux-textspans--STRIKETHROUGH")
            original_price = (original_price_element.text if original_price_element else "Not available")

            savings_element = soup.select_one(".x-additional-info__textual-display .ux-textspans--EMPHASIS")
            savings = savings_element.text if savings_element else "Not available"

            # URL Product Image
            image_grid_container = soup.find("div", class_="ux-image-grid-container")

            image_links = []

            if image_grid_container:
                img_elements = image_grid_container.select(".ux-image-grid-item img")
                image_links = [img["src"] for img in img_elements if "src" in img.attrs]

            # Seller
            item_seller_element = soup.select_one(".x-sellercard-atf__info__about-seller .ux-textspans--BOLD")
            seller = item_seller_element.text if item_seller_element else "Not available"

            # Seller Feedback
            seller_feedback_element = soup.select_one('.x-sellercard-atf__data-item-wrapper li[data-testid="x-sellercard-atf__data-item"] a')
            seller_feedback = (seller_feedback_element.text if seller_feedback_element else "Not available")

            # Shipping
            shipping_parent_element = soup.find("div", class_="ux-labels-values--shipping")
            shipping = (
                "Free Shipping"
                if not shipping_parent_element
                else shipping_parent_element.find("span", class_="ux-textspans--BOLD").text
            )

            item_data["title"] = title,
            item_data["current_price"] = current_price,
            item_data["original_price"] = original_price,
            item_data["savings"] = savings,
            item_data["image_links"] = image_links,
            item_data["product_url"] = self.product_url,
            item_data["seller"] = seller,
            item_data["seller_feedback"] = seller_feedback
            item_data["shipping"] = shipping

            return item_data
        except Exception as e:
            print(f"Error: Unable to parse eBay data ({e})")
            return None

    def save_to_json(self, filename="InterBox/product_info.json"):
        item_data = self.parse_product_data()
        if item_data:
            with open(filename, "w") as file:
                json.dump(item_data, file, indent=4)
                print(f"Success: eBay item information saved to {filename}")


if __name__ == "__main__":
    item = "404925427501"
    product_page = f"https://www.ebay.com/itm/{item}"
    scraper = eBayProductScraper(product_page)
    scraper.save_to_json()

