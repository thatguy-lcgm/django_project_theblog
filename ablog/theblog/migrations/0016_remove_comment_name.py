# Generated by Django 4.1.5 on 2023-03-15 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("theblog", "0015_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="name",
        ),
    ]
