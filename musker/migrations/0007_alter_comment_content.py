# Generated by Django 5.1.5 on 2025-02-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("musker", "0006_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="content",
            field=models.TextField(),
        ),
    ]
