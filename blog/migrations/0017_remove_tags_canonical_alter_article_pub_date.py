# Generated by Django 4.2.4 on 2023-09-01 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_tags_alter_article_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='canonical',
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 1, 21, 18, 3, 283131)),
        ),
    ]
