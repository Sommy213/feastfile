# Generated by Django 4.2.4 on 2023-10-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feastfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
