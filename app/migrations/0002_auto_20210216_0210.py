# Generated by Django 2.2 on 2021-02-16 10:10

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='tz',
            field=timezone_field.fields.TimeZoneField(),
        ),
    ]
