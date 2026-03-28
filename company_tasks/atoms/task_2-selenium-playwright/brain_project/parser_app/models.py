"""This module contains models for the parser app."""

from django.contrib.postgres.fields import ArrayField
from django.db import models


class Product(models.Model):
    """Model representing a product scraped from the website."""

    title = models.CharField(max_length=255, null=True)
    memory = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=100, null=True)
    vendor = models.CharField(max_length=100, null=True)
    promo_price = models.CharField(max_length=50, null=True)
    original_price = models.CharField(max_length=50, null=True)

    images = ArrayField(
        models.CharField(max_length=500, null=True), null=True, blank=True
    )  # noqa: E501
    specifications = models.JSONField(default=dict, null=True, blank=True)
    reviews_count = models.CharField(null=True)
    screen_diagonal = models.CharField(max_length=50, null=True)
    screen_resolution = models.CharField(max_length=50, null=True)
    product_code = models.CharField(max_length=100, null=True)

    link = models.URLField(null=True, blank=True, unique=True)
    status = models.CharField(max_length=50, default="New", null=True)

    def __str__(self):  # noqa: D105
        return self.title
