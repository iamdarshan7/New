# Generated by Django 2.2.17 on 2020-11-25 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_page', '0026_auto_20201125_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutcarousel',
            name='is_active',
        ),
    ]