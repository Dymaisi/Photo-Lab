# Generated by Django 3.2.12 on 2022-04-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_member_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='uploader',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
