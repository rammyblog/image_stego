# Generated by Django 2.2.11 on 2020-03-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200307_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='autentication_image',
            field=models.ImageField(blank=True, null=True, upload_to='auth-images'),
        ),
    ]
