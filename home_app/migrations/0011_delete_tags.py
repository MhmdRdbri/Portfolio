# Generated by Django 4.2.4 on 2023-09-01 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0010_alter_tags_site_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
