# Generated by Django 2.2.16 on 2020-11-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_pictures_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='image',
            field=models.ImageField(default=1990, upload_to='images/'),
            preserve_default=False,
        ),
    ]
