# Generated by Django 5.1.5 on 2025-02-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("musker", "0003_alter_profile_date_modified_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="date_modified",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="facebook_link",
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="homepage_link",
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="instagram_link",
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="linkedin_link",
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]
