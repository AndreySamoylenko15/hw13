# Generated by Django 5.0.3 on 2024-03-31 13:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0010_quote_name_tag_tag_of_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quote",
            name="name",
        ),
    ]