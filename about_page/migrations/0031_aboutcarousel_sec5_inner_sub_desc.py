# Generated by Django 2.2.17 on 2020-11-26 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_page', '0030_auto_20201126_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutcarousel',
            name='sec5_inner_sub_desc',
            field=models.TextField(default=2020),
            preserve_default=False,
        ),
    ]
