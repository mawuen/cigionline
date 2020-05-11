# Generated by Django 3.0.6 on 2020-05-06 15:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtaildocs', '0010_document_file_hash'),
        ('core', '0006_fundingpage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basicpage',
            options={'verbose_name': 'Page', 'verbose_name_plural': 'Pages'},
        ),
        migrations.CreateModel(
            name='AnnualReportPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('feature_subtitle', models.CharField(blank=True, max_length=255)),
                ('feature_title', models.CharField(blank=True, max_length=255)),
                ('report_interactive', models.CharField(blank=True, help_text='Internal path to the interactive report. Example: /interactives/2019annualreport', max_length=255)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2005), django.core.validators.MaxValueValidator(2050)])),
                ('image_feature', models.ForeignKey(blank=True, help_text='Image used when featuring on landing pages such as the home page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Feature image')),
                ('image_poster', models.ForeignKey(blank=True, help_text='Poster sized image that is displayed in the featured section on the Annual Reports page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Cover image')),
                ('report_english', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('report_financial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('report_french', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'verbose_name': 'Annual Report Page',
                'verbose_name_plural': 'Annual Report Pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AnnualReportListPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('block_quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.RichTextBlock(required=True)), ('quote_author', wagtail.core.blocks.CharBlock(required=False)), ('author_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], blank=True)),
                ('subtitle', wagtail.core.fields.RichTextField(blank=True)),
                ('image_hero', models.ForeignKey(blank=True, help_text='A large image to be displayed prominently on the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Hero Image')),
            ],
            options={
                'verbose_name': 'Annual Report List Page',
            },
            bases=('wagtailcore.page',),
        ),
    ]