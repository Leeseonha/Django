# Generated by Django 2.2.1 on 2019-05-31 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
