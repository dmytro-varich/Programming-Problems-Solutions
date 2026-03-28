"""Loads Django settings and sets up the Django environment for testing."""

import os
import sys

import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "brain_project")))  # noqa: E501

os.environ["DJANGO_SETTINGS_MODULE"] = "brain_project.settings"
django.setup()
