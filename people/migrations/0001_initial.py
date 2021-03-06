# Generated by Django 3.1.1 on 2020-09-22 01:09

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import streams.blocks
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtaildocs', '0010_document_file_hash'),
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0052_pagelogentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeoplePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Person List Page',
                'verbose_name_plural': 'Person List Pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PersonListPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.StreamField([('paragraph', streams.blocks.ParagraphBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('block_quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.RichTextBlock(required=True)), ('quote_author', wagtail.core.blocks.CharBlock(required=False)), ('author_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(required=False))])), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('text_border_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=True)), ('border_colour', wagtail.core.blocks.CharBlock(required=True))]))], blank=True)),
                ('subtitle', wagtail.core.fields.RichTextField(blank=True)),
                ('person_list_page_type', models.IntegerField(choices=[(0, 'Default'), (1, 'Experts'), (2, 'Staff'), (3, 'Leadership')], default=0)),
            ],
            options={
                'verbose_name': 'Person List Page',
                'verbose_name_plural': 'Person List Pages',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='PersonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('drupal_taxonomy_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('archive', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)),
                ('address_city', models.CharField(blank=True, max_length=255)),
                ('address_country', models.CharField(blank=True, max_length=255)),
                ('address_line1', models.CharField(blank=True, max_length=255)),
                ('address_line2', models.CharField(blank=True, max_length=255)),
                ('address_postal_code', models.CharField(blank=True, max_length=32)),
                ('address_province', models.CharField(blank=True, max_length=255)),
                ('board_position', models.CharField(blank=True, max_length=255)),
                ('body', wagtail.core.fields.StreamField([('paragraph', streams.blocks.ParagraphBlock())], blank=True, verbose_name='Full Biography')),
                ('education', wagtail.core.fields.StreamField([('education', wagtail.core.blocks.StructBlock([('degree', wagtail.core.blocks.CharBlock(required=True)), ('school', wagtail.core.blocks.CharBlock(required=True)), ('school_website', wagtail.core.blocks.URLBlock(required=False)), ('year', wagtail.core.blocks.IntegerBlock(required=False))]))], blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('expertise', wagtail.core.fields.StreamField([('expertise', wagtail.core.blocks.CharBlock(required=True))], blank=True)),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('languages', wagtail.core.fields.StreamField([('language', wagtail.core.blocks.CharBlock(required=True))], blank=True)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('linkedin_url', models.URLField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=32)),
                ('position', models.CharField(blank=True, max_length=255)),
                ('short_bio', wagtail.core.fields.RichTextField(blank=True, verbose_name='Short Biography')),
                ('external_publications', wagtail.core.fields.StreamField([('external_publication', wagtail.core.blocks.StructBlock([('author', wagtail.core.blocks.CharBlock(required=True)), ('location_in_work', wagtail.core.blocks.CharBlock(required=False)), ('publisher_info', wagtail.core.blocks.CharBlock(required=False)), ('publication_type', wagtail.core.blocks.ChoiceBlock(choices=[('Generic', 'Generic'), ('Book', 'Book'), ('Book Section', 'Book Section'), ('Edited Book', 'Edited Book'), ('Electronic Article', 'Electronic Article'), ('Electronic Book', 'Electronic Book'), ('Journal Article', 'Journal Article'), ('Newspaper Article', 'Newspaper Article'), ('Report', 'Report'), ('Thesis', 'Thesis'), ('Web Page', 'Web Page')])), ('secondary_author', wagtail.core.blocks.CharBlock(required=False)), ('secondary_title', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.URLBlock(required=False)), ('url_title', wagtail.core.blocks.CharBlock(required=False)), ('year', wagtail.core.blocks.IntegerBlock(required=False))]))], blank=True)),
                ('twitter_username', models.CharField(blank=True, max_length=255)),
                ('website', models.URLField(blank=True)),
                ('drupal_node_id', models.IntegerField(blank=True, null=True)),
                ('curriculum_vitae', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document')),
                ('image_media', models.ForeignKey(blank=True, help_text="A high resolution image that is downloadable from the expert's page.", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Media photo')),
                ('image_square', models.ForeignKey(blank=True, help_text='For circular profile images that are used throughout the website.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Square image')),
                ('person_types', modelcluster.fields.ParentalManyToManyField(blank=True, to='people.PersonType')),
            ],
            options={
                'verbose_name': 'Person Page',
                'verbose_name_plural': 'Person Pages',
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
