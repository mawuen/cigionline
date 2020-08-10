# Generated by Django 3.0.6 on 2020-06-02 14:42

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_annualreportlistpage_submenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualreportlistpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('block_quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.RichTextBlock(required=True)), ('quote_author', wagtail.core.blocks.CharBlock(required=False)), ('author_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('table', wagtail.contrib.table_block.blocks.TableBlock())], blank=True),
        ),
        migrations.AlterField(
            model_name='basicpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('block_quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.RichTextBlock(required=True)), ('quote_author', wagtail.core.blocks.CharBlock(required=False)), ('author_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('table', wagtail.contrib.table_block.blocks.TableBlock())], blank=True),
        ),
        migrations.AlterField(
            model_name='fundingpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('block_quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.RichTextBlock(required=True)), ('quote_author', wagtail.core.blocks.CharBlock(required=False)), ('author_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('table', wagtail.contrib.table_block.blocks.TableBlock())], blank=True),
        ),
    ]
