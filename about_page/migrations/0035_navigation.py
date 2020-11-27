# Generated by Django 2.2.17 on 2020-11-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_page', '0034_testimonial_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, null=True, unique=True)),
                ('logo', models.ImageField(upload_to='Images/')),
            ],
        ),
    ]