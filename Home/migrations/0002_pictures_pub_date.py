# Generated by Django 2.2.16 on 2020-11-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
    ]