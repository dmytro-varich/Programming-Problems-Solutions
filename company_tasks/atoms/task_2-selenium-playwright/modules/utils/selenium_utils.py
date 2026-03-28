"""This file contains utility functions for Selenium operations."""

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.processing_utils import DataProcessingUtils as dpu


class ScraperUtils:
    """Utility functions for Selenium operations."""

    @staticmethod
    def get_element_text(wait: WebDriverWait, locator: tuple) -> str | None:
        """Gets the text content of a web element.

        Args:
            wait: WebDriverWait instance for waiting on the element.
            locator: A tuple containing the By strategy and the locator string.

        Returns:
            The text content of the element or None if not found.

        Example:
            title = ScraperUtils.get_element_text(
              wait,
              (By.CSS_SELECTOR, "h1.title")
            )
        """
        try:
            element = wait.until(EC.presence_of_element_located(locator))
            return dpu.clean_text(element.get_attribute("textContent"))
        except TimeoutException:
            print("Error: Element not found within the specified timeout.")
            return None

    @staticmethod
    def get_attributes_list(
        wait: WebDriverWait,
        parent_locator: tuple,
        child_locator: tuple,
        attr: str = "src"
    ) -> list:
        """Gets a list of specified attributes from child elements within a parent element.

        Args:
            wait: WebDriverWait instance for waiting on elements.
            parent_locator: Locator tuple to locate the parent element.
            child_locator: Locator tuple to locate child elements within the parent.
            attr: The attribute name to extract from each child element.

        Returns:
            A list of attribute values or [] if no elements are found or an error occurs.

        Example:
            images = ScraperUtils.get_attributes_list(
               wait,
               (By.CSS_SELECTOR, "div.product-block-bottom"),
               (By.TAG_NAME, "img"),
               attr="src"
            )
        """  # noqa: E501
        try:
            parent = wait.until(EC.presence_of_element_located(parent_locator))
            by, value = child_locator
            elements = parent.find_elements(*child_locator)
            results = [
                el.get_attribute(attr) for el in elements if el.get_attribute(attr)
            ]
            return results if results else []
        except TimeoutException:
            print("Error: Parent element not found within the specified timeout.")
            return []

    @staticmethod
    def get_element_dict(
        parent_element: WebElement,
        locator_main_key: tuple | None = None,
        locator_row: tuple | None = None,
        locator_sub_key: tuple | None = None,
        locator_sub_value: tuple | None = None,
        make_nested: bool = True
    ) -> dict:
        """Extracts a dictionary of key-value pairs from structured web elements.

        Args:
            parent_element: The WebElement that contains the data to extract.
            locator_main_key: Optional locator for the main key (e.g., section header).
            locator_row: Optional locator for the rows containing key-value pairs.
            locator_sub_key: Optional locator for the sub-key within each row.
            locator_sub_value: Optional locator for the sub-value within each row.
            make_nested: If True, creates a nested dictionary under the main key.

        Returns:
            A dictionary containing the extracted key-value pairs, optionally nested under a main key.

        Example:
            data = ScraperUtils.get_element_dict(
               parent_element=section_element,
               locator_main_key=(By.TAG_NAME, "h3"),
               locator_row=(By.CSS_SELECTOR, "div.row"),
               locator_sub_key=(By.CSS_SELECTOR, "span.key"),
               locator_sub_value=(By.CSS_SELECTOR, "span.value"),
               make_nested=True
            )
        """  #Noqa: E501
        result_dict = {}

        try:
            # 1. Define main key if locator is provided
            main_key_text = None
            if locator_main_key:
                try:
                    raw_text = ScraperUtils.get_element_text(
                        WebDriverWait(parent_element, 1), locator_main_key
                    )
                    main_key_text = dpu.clean_text(raw_text.strip())
                except NoSuchElementException:
                    main_key_text = None

            # 2. Prepare the dictionary structure
            # If a nested dictionary is needed and a header is present, create a branch
            if make_nested and main_key_text:
                result_dict[main_key_text] = {}
                target_dict = result_dict[main_key_text]
            else:
                # If a flat structure is needed or no header is present — write to the root  # noqa: E501
                target_dict = result_dict

            # 3. Search for data rows
            if not locator_row:
                return result_dict # If no rows are found, return what we have (header)

            rows = parent_element.find_elements(*locator_row)

            for row in rows:
                try:
                    # Extract key and value using provided locators
                    k = ScraperUtils.get_element_text(
                        WebDriverWait(row, 1), locator_sub_key
                    )
                    v = ScraperUtils.get_element_text(
                        WebDriverWait(row, 1), locator_sub_value
                    )

                    if k:
                        target_dict[k] = v

                except NoSuchElementException:
                    continue # Skip rows that don't have the expected structure
                except Exception as e:
                    print(f"Error occurred while processing row: {e}")
                    continue

            # 4. Final check: if we created a header but there's no data in it
            if make_nested and main_key_text and not result_dict[main_key_text]:
                return {}

            return result_dict

        except Exception as e:
            print(f"Global error in get_element_dict: {e}")
            return {}
