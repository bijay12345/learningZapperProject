# Generated by Django 4.2 on 2023-04-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_resource_count_lesson_resources_count_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='resources',
            index=models.Index(fields=['resource_type'], name='main_resour_resourc_651bcd_idx'),
        ),
    ]
