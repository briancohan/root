from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    hero_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Write an introduction for the site",
    )
    hero_cta = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Hero CTA",
        help_text="Test to display on the Call to Action",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA Link",
        help_text="Choose a page to link to for the Call to Action",
    )

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link"),
            ],
            heading="Hero Section",
        ),
        FieldPanel("body", classname="full"),
    ]
