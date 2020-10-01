# Generated by Django 3.1.1 on 2020-09-22 01:09

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('people', '0001_initial'),
        ('menus', '0002_populate_menus'),
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personpage',
            name='projects',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='research.ProjectPage'),
        ),
        migrations.AddField(
            model_name='personpage',
            name='topics',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='research.TopicPage'),
        ),
        migrations.AddField(
            model_name='personlistpage',
            name='image_hero',
            field=models.ForeignKey(blank=True, help_text='A large image to be displayed prominently on the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Hero Image'),
        ),
        migrations.AddField(
            model_name='personlistpage',
            name='submenu',
            field=models.ForeignKey(blank=True, help_text='Select a submenu to appear in the right section of the hero.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='menus.menu', verbose_name='Submenu'),
        ),
    ]