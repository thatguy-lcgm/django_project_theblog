# Generated by Django 4.1.5 on 2023-03-15 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("theblog", "0018_alter_comment_name"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Comment",
        ),
    ]
