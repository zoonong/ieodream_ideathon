# Generated by Django 3.2.5 on 2021-08-10 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0002_auto_20210809_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
