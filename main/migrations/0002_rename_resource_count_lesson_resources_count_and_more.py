# Generated by Django 4.2 on 2023-04-11 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='resource_count',
            new_name='resources_count',
        ),
        migrations.RemoveField(
            model_name='class',
            name='resources',
        ),
        migrations.AddField(
            model_name='lesson',
            name='resources',
            field=models.ManyToManyField(related_name='lessons', to='main.resources'),
        ),
        migrations.RemoveField(
            model_name='class',
            name='lessons',
        ),
        migrations.AddField(
            model_name='class',
            name='lessons',
            field=models.ManyToManyField(related_name='classes', to='main.lesson'),
        ),
    ]
