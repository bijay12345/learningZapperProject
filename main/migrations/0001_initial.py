# Generated by Django 4.2 on 2023-04-11 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('resource_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('resource_type', models.CharField(choices=[('P', 'PDF'), ('V', 'VIDEO')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('lessons', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.lesson')),
                ('resources', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.resources')),
            ],
        ),
    ]
