# Generated by Django 2.2.17 on 2020-11-24 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutsec2',
            name='sec2_dynamic_image',
            field=models.ImageField(default=2020, upload_to='images/'),
            preserve_default=False,
        ),
    ]
