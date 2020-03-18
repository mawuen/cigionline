from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class TopicListPage(Page):
    """Topic list page"""

    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['research.TopicPage']
    templates = 'research/topic_list_page.html'

    class Meta:
        verbose_name = 'Topic List Page'


class TopicPage(Page):
    """View topic page"""
    description = RichTextField(blank=True, null=False)

    content_panels = Page.content_panels + [
        FieldPanel('description')
    ]
    parent_page_types = ['research.TopicListPage']
    subpage_types = []
    templates = 'research/topic_page.html'

    class Meta:
        verbose_name = 'Topic Page'
        verbose_name_plural = 'Topic Pages'