# Generated by Django 4.1.6 on 2023-03-11 01:07

import blog.models
import datetime
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_blogpost_cover_image_alter_blogpost_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='space-our-blog-backend/media'), upload_to='blog-images/', validators=[blog.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 11, 1, 7, 18, 485758, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='blogpostimage',
            name='images',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='space-our-blog-backend/media'), upload_to='blog-images/', validators=[blog.models.validate_image]),
        ),
    ]
