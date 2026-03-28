"""This module contains utility functions."""

import re


class DataProcessingUtils:
    """Utility functions for data processing."""

    @staticmethod
    def extract_price(text: str, dtype: str | int = str) -> str | None:
        """Extracts the price from the input text."""
        if not text:
            return None

        price = "".join(filter(str.isdigit, text))

        if dtype is int:
            try:
                return int(price)
            except ValueError:
                return None

        return price if price else None


    @staticmethod
    def clean_text(text: str) -> str:
        """Cleans the input text by removing extra whitespace and non-breaking spaces."""  # noqa: E501
        return re.sub(r'\s+', ' ', text.replace('\xa0', ' ')).strip()
