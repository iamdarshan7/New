# Generated by Django 2.2.17 on 2020-11-24 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_page', '0011_auto_20201124_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutsec3',
            name='sec3_desc',
        ),
        migrations.RemoveField(
            model_name='aboutsec3',
            name='sec3_title',
        ),
    ]
