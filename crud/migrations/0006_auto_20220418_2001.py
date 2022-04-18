# Generated by Django 3.2.12 on 2022-04-18 12:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20220418_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='StyleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=40)),
                ('img', models.ImageField(upload_to='styles/')),
            ],
        ),
        migrations.AddField(
            model_name='styleupload',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
