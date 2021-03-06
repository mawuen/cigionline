from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    InlinePanel,
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Orderable


class Menu(ClusterableModel):
    name = models.CharField(max_length=32)
    slug = models.CharField(max_length=32)

    panels = [
        MultiFieldPanel(
            [
                InlinePanel('menu_items'),
            ],
            heading='Menu Items',
        ),
    ]

    def __str__(self):
        return self.name


class MenuItem(Orderable):
    title = models.CharField(max_length=32)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE,
    )
    link_url = models.CharField(
        blank=True,
        max_length=512,
        help_text='An external URL (https://...) or an internal URL (/interactives/2019annualreport/). This field is only considered if there is no link page.',
    )
    menu = ParentalKey('Menu', related_name='menu_items', on_delete=models.CASCADE)
    submenu = models.ForeignKey(
        'menus.Menu',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE,
        help_text='Related submenu to show in the hamburger menu.'
    )

    panels = [
        FieldPanel('title'),
        PageChooserPanel('link_page'),
        FieldPanel('link_url'),
        FieldPanel('submenu'),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'
