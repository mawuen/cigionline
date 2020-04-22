from core.models import CorePage
from django.db import models
from django.db.models.functions import Lower
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class PeoplePage(Page):
    """
    A special singleton page that isn't published, but is the parent to all the
    person pages at the path /people.
    """
    max_count = 1
    parent_page_types = ['core.HomePage']
    subpage_types = ['people.PersonPage']
    templates = 'people/person_list_page.html'

    class Meta:
        verbose_name = 'Person List Page'
        verbose_name_plural = 'Person List Pages'


class PersonListPage(CorePage):
    """
    The pages that show people. There are currently 2 on our website:
    /experts and /about/staff. This was made into a separate page model so that
    PersonPage's could not be created as children of these paths.
    """

    class PersonListPageType(models.IntegerChoices):
        DEFAULT = 0
        EXPERTS = 1
        STAFF = 2

    person_list_page_type = models.IntegerField(choices=PersonListPageType.choices, default=PersonListPageType.DEFAULT)

    max_count = 2
    parent_page_types = ['core.BasicPage', 'core.HomePage']
    subpage_types = []
    templates = 'people/person_list_page.html'

    class Meta:
        verbose_name = 'Person List Page'
        verbose_name_plural = 'Person List Pages'

    @property
    def person_pages(self):
        if self.person_list_page_type == PersonListPage.PersonListPageType.EXPERTS:
            return PersonPage.objects.live().filter(
                archive=PersonPage.ArchiveStatus.UNARCHIVED,
                person_types__name__in=['CIGI Chair', 'Expert'],
            ).order_by(Lower('last_name'), Lower('first_name'))
        elif self.person_list_page_type == PersonListPage.PersonListPageType.STAFF:
            return PersonPage.objects.live().filter(
                archive=PersonPage.ArchiveStatus.UNARCHIVED,
                person_types__name='Staff',
            ).order_by(Lower('last_name'), Lower('first_name'))
        return []

    def get_template(self, request, *args, **kwargs):
        original_template = super(PersonListPage, self).get_template(request, *args, **kwargs)
        if self.person_list_page_type == PersonListPage.PersonListPageType.EXPERTS:
            return 'people/person_list_experts_page.html'
        elif self.person_list_page_type == PersonListPage.PersonListPageType.STAFF:
            return 'people/person_list_staff_page.html'
        return original_template


class PersonPage(Page):
    """View person page"""

    class ArchiveStatus(models.IntegerChoices):
        UNARCHIVED = (0, 'No')
        ARCHIVED = (1, 'Yes')

    address_city = models.CharField(blank=True, max_length=255)
    address_country = models.CharField(blank=True, max_length=255)
    address_line1 = models.CharField(blank=True, max_length=255)
    address_line2 = models.CharField(blank=True, max_length=255)
    address_postal_code = models.CharField(blank=True, max_length=32)
    address_province = models.CharField(blank=True, max_length=255)
    archive = models.IntegerField(choices=ArchiveStatus.choices, default=ArchiveStatus.UNARCHIVED)
    board_position = models.CharField(blank=True, max_length=255)
    body = StreamField(
        [
            ('paragraph', blocks.RichTextBlock())
        ],
        blank=True,
        verbose_name='Full Biography'
    )
    curriculum_vitae = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    education = StreamField([
        ('education', blocks.StructBlock([
            ('degree', blocks.CharBlock(required=True)),
            ('school', blocks.CharBlock(required=True)),
            ('school_website', blocks.URLBlock(required=False)),
            ('year', blocks.IntegerBlock(required=False))
        ]))
    ], blank=True)
    email = models.EmailField(blank=True)
    expertise = StreamField([
        ('expertise', blocks.CharBlock(required=True))
    ], blank=True)
    first_name = models.CharField(blank=True, max_length=255)
    image_media = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Media Photo',
        help_text='A high resolution image that is downloadable from the expert\'s page.'
    )
    image_square = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Square Image',
        help_text='For circular profile images that are used throughout the website.'
    )
    languages = StreamField([
        ('language', blocks.CharBlock(required=True))
    ], blank=True)
    last_name = models.CharField(blank=True, max_length=255)
    linkedin_url = models.URLField(blank=True)
    person_types = ParentalManyToManyField('people.PersonType', blank=True)
    phone_number = models.CharField(blank=True, max_length=32)
    position = models.CharField(blank=True, max_length=255)
    short_bio = RichTextField(blank=True, verbose_name='Short Biography')
    topics = ParentalManyToManyField('research.TopicPage', blank=True)
    twitter_username = models.CharField(blank=True, max_length=255)
    website = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('first_name'),
                FieldPanel('last_name'),
                FieldPanel('position'),
                FieldPanel('board_position')
            ],
            heading='General Information',
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('short_bio'),
                StreamFieldPanel('body')
            ],
            heading='Biography',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('address_line1'),
                FieldPanel('address_line2'),
                FieldPanel('address_city'),
                FieldPanel('address_province'),
                FieldPanel('address_postal_code'),
                FieldPanel('address_country')
            ],
            heading='Address',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('email'),
                FieldPanel('phone_number'),
                FieldPanel('twitter_username'),
                FieldPanel('linkedin_url'),
                FieldPanel('website')
            ],
            heading='Contact Information',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('person_types'),
                StreamFieldPanel('languages'),
                DocumentChooserPanel('curriculum_vitae')
            ],
            heading='Additional Information',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel('education')
            ],
            heading='Education',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel('expertise')
            ],
            heading='Expertise',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel('image_square'),
                ImageChooserPanel('image_media')
            ],
            heading='Images',
            classname='collapsible collapsed'
        ),
        MultiFieldPanel(
            [
                FieldPanel('topics')
            ],
            heading='Related',
            classname='collapsible collapsed'
        )
    ]
    settings_panels = Page.settings_panels + [
        FieldPanel('archive'),
    ]
    parent_page_types = ['people.PeoplePage']
    subpage_types = []
    templates = 'people/person_page.html'

    class Meta:
        verbose_name = 'Person Page'
        verbose_name_plural = 'Person Pages'


class PersonType(models.Model):
    """
    A Django model that stores the person types. This isn't allowed to be
    edited in the admin interface. To insert/remove data - a migration needs to
    be created.

    The available person types are:
    - Board Member
    - CIGI Chair
    - Commission
    - Expert
    - External profile
    - G20 Expert
    - Management Team
    - Media Contact
    - Person
    - Program Director
    - Program Manager
    - Research Advisor
    - Research Associate
    - Research Fellow
    - Speaker
    - Staff
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name