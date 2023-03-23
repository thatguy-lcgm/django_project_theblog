# Generated by Django 4.1.5 on 2023-02-08 06:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("theblog", "0004_category_post_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                related_name="blog_post", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
