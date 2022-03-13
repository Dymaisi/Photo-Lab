from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    # Home page model
    templates = "image_style\style.html"
    # templates = "image_style\\option\\option.html"

