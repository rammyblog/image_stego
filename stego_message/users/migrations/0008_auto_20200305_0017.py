# Generated by Django 2.2.11 on 2020-03-04 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200304_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='autentication_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
