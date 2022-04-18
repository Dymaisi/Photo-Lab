# Generated by Django 3.2.12 on 2022-04-18 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_auto_20220414_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='upload_color_img',
        ),
        migrations.RemoveField(
            model_name='member',
            name='upload_restore_img',
        ),
        migrations.RemoveField(
            model_name='member',
            name='upload_style_img',
        ),
        migrations.AlterField(
            model_name='colorupload',
            name='user',
            field=models.CharField(default='123', max_length=40),
        ),
        migrations.AlterField(
            model_name='restoreupload',
            name='user',
            field=models.CharField(default='123', max_length=40),
        ),
        migrations.AlterField(
            model_name='styleupload',
            name='user',
            field=models.CharField(default='123', max_length=40),
        ),
    ]
