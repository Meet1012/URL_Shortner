# Generated by Django 5.1.3 on 2024-11-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_alter_url_schema_createdat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='url_schema',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
