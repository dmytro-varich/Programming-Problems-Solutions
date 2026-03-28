"""This file contains utility functions for Playwright operations."""

from playwright.sync_api import Locator, TimeoutError
from utils.processing_utils import DataProcessingUtils as dpu


class ScraperUtils:
    """Utility functions for Playwright operations."""

    @staticmethod
    def get_element_text(
        locator: Locator, state: str = "attached", timeout: int = 5000
    ) -> str | None:
        """Gets text content of an element.

        Args:
            locator: Playwright Locator object for the target element.
            state: The state to wait for (default: "attached").
            timeout: Time to wait for the element in milliseconds (default: 5000).

        Returns:
            Cleaned text content of the element or None if not found.

        Example:
            title = ScraperUtils.get_element_text(page.locator("h1.title"), timeout=10000)
        """  # noqa: E501
        try:
            locator.wait_for(state=state, timeout=timeout)
            if locator.count() == 0:
                print("Error: Element not found.")
                return None

            text = locator.first.text_content()
            return dpu.clean_text(text) if text else None
        except TimeoutError:
            print("Error: Element not found within the specified timeout.")
            return None

    @staticmethod
    def get_attributes_list(
        parent_locator: Locator, child_selector: str, attr: str = "src"
    ) -> list:
        """Gets list of attributes from child elements.

        Args:
            parent_locator: Playwright Locator to locate the parent element.
            child_selector: CSS selector to locate child elements within the parent.
            attr: The attribute name to extract (default: "src").

        Returns:
            A list of attribute values or [] if no elements are found or an error occurs.

        Example:
            images = ScraperUtils.get_attributes_list(
               parent_locator=page.locator("div.product-block-bottom"),
               child_selector="img",
               attr="src"
            )
        """  # noqa: E501
        try:
            children = parent_locator.locator(child_selector)

            return [
                el.get_attribute(attr)
                for el in children.all()
                if el.get_attribute(attr)
            ]

        except Exception as e:
            print(f"Error while getting attributes list: {e}")
            return []

    @staticmethod
    def get_element_dict(
        parent: Locator,
        selector_main_key: str | None = None,
        selector_row: str | None = None,
        selector_sub_key: str | None = None,
        selector_sub_value: str | None = None,
        make_nested: bool = True,
    ) -> dict:
        """Extracts structured data from a parent element based on provided selectors.

        Args:
            parent: Playwright Locator for the parent element containing the data.
            selector_main_key: Optional CSS selector for the main key (header) of the data block.
            selector_row: Optional CSS selector for the rows containing key-value pairs.
            selector_sub_key: Optional CSS selector for the sub-key within each row.
            selector_sub_value: Optional CSS selector for the sub-value within each row.
            make_nested: Whether to create a nested dictionary structure (default: True).

        Returns:
            A dictionary containing the extracted structured data.

        Example:
            specs = ScraperUtils.get_element_dict(
               parent=page.locator("div.br-pr-chr"),
               selector_main_key="h3",
               selector_row="div.br-pr-chr-item div[span[2]]",
               selector_sub_key="span:first-child",
               selector_sub_value="span:last-child"
            )
        """  # noqa: E501
        result_dict = {}

        try:
            main_key_text = None

            # 1. Define main key if locator is provided
            if selector_main_key:
                try:
                    text = ScraperUtils.get_element_text(
                        parent.locator(selector_main_key)
                    )
                    main_key_text = text if text else None
                except Exception:
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
            if not selector_row:
                return result_dict # If no rows are found, return what we have (header)

            rows = parent.locator(selector_row)

            for row in rows.all():
                # Extract key and value using provided locators
                try:
                    k = (
                        ScraperUtils.get_element_text(row.locator(selector_sub_key))
                        if selector_sub_key
                        else None
                    )

                    v = (
                        ScraperUtils.get_element_text(row.locator(selector_sub_value))
                        if selector_sub_value
                        else None
                    )

                    if k:
                        target_dict[k] = v

                except Exception as e:
                     print(f"Error occurred while processing row: {e}")
                     continue  # Skip rows that don't have the expected structure

            # 4. Final check: if we created a header but there's no data in it
            if make_nested and main_key_text and not result_dict[main_key_text]:
                return {}

            return result_dict

        except Exception as e:
            print(f"Global error in get_element_dict: {e}")
            return {}

    @staticmethod
    def select_locator(
        locator: Locator,
        *,
        index: int | None = None,
        first_visible: bool = False,
        text: str | None = None,
        exact: bool = True
    ) -> Locator | None:
        """Selects a locator based on index, visibility, or text content.

        Args:
            locator: Playwright Locator object to select from.
            index: Optional index of the element to select (0-based).
            first_visible: If True, selects the first visible element.
            text: Optional text to match for selection.
            exact: If True, matches text exactly; if False, matches if text is contained.

        Returns:
            A Locator object for the selected element or None if no matching element is found.

        Example:
            # Select by index
            el = ScraperUtils.select_locator(page.locator("div.items > div"), index=2)

            # Select first visible
            el = ScraperUtils.select_locator(page.locator("div.items > div"), first_visible=True)

            # Select by exact text
            el = ScraperUtils.select_locator(page.locator("div.items > div"), text="Example", exact=True)

            # Select by partial text
            el = ScraperUtils.select_locator(page.locator("div.items > div"), text="Example", exact=False)
        """  # Noqa: E501
        count = locator.count()
        if count == 0:
            return None

        # By index
        if index is not None:
            if 0 <= index < count:
                return locator.nth(index)
            return None

        # By text content
        if text is not None:
            for i in range(count):
                el = locator.nth(i)
                el_text = el.text_content()
                if el_text:
                    if (exact and el_text.strip() == text) or (not exact and text in el_text):  # Noqa: E501
                        return el
            return None

        # First visible element
        if first_visible:
            for i in range(count):
                el = locator.nth(i)
                if el.is_visible():
                    return el
            return None

        # If nothing is specified — return the first element
        return locator.first
