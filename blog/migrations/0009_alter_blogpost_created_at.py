# Generated by Django 4.1.6 on 2023-03-12 00:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_blogpostsbsguidesubsection_blog_step_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 0, 36, 47, 449103, tzinfo=datetime.timezone.utc)),
        ),
    ]
