# Generated by Django 3.0.5 on 2020-04-17 20:47

from django.db import migrations


def populate_person_types(apps, schema_editor):
    DEFAULT_TYPES = [
        'Board Member',
        'CIGI Chair',
        'Commission',
        'Expert',
        'External profile',
        'G20 Expert',
        'Management Team',
        'Media Contact',
        'Person',
        'Program Director',
        'Program Manager',
        'Research Advisor',
        'Research Associate',
        'Research Fellow',
        'Speaker',
        'Staff',
    ]
    PersonType = apps.get_model('people', 'PersonType')
    for default_type in DEFAULT_TYPES:
        person_type = PersonType(name=default_type)
        person_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_person_types),
    ]