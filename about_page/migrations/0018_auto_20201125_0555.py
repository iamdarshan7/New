# Generated by Django 2.2.17 on 2020-11-25 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_page', '0017_auto_20201125_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutsec1',
            name='sec1_title',
            field=models.CharField(max_length=100),
        ),
    ]
