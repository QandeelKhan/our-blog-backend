# Generated by Django 4.1.6 on 2023-03-12 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 13, 57, 8, 829349, tzinfo=datetime.timezone.utc), help_text='The date and time when the blog post was created.'),
        ),
    ]
