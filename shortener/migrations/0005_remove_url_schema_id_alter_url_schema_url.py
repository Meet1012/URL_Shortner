# Generated by Django 5.1.3 on 2024-11-20 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_url_schema_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url_schema',
            name='id',
        ),
        migrations.AlterField(
            model_name='url_schema',
            name='url',
            field=models.URLField(primary_key=True, serialize=False),
        ),
    ]
