# Generated by Django 4.1.6 on 2023-03-10 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_featured_blogpost_featured_posts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='paragraph_after_image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='post_images',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_images', to='blog.blogpostimage'),
        ),
    ]
