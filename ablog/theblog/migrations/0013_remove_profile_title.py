# Generated by Django 4.1.5 on 2023-03-03 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("theblog", "0012_profile_facebook_url_profile_instagram_url_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="title",
        ),
    ]
