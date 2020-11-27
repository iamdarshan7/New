# Generated by Django 2.2.17 on 2020-11-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_page', '0024_auto_20201125_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec2_inner_title', models.CharField(max_length=100)),
                ('sec2_inner_desc', models.TextField()),
                ('sec2_inner_image', models.ImageField(null=True, upload_to='Images/')),
                ('sec5_inner_name', models.CharField(max_length=100)),
                ('sec5_inner_profession', models.CharField(max_length=100)),
                ('sec5_inner_desc', models.TextField()),
                ('sec5_inner_image', models.ImageField(null=True, upload_to='Images/')),
            ],
        ),
        migrations.CreateModel(
            name='AboutMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_heading', models.CharField(max_length=100)),
                ('top_bg_image', models.ImageField(null=True, upload_to='Images/')),
                ('sec1_title', models.CharField(max_length=100)),
                ('sec1_desc', models.TextField()),
                ('sec1_inner1_title', models.CharField(max_length=100)),
                ('sec1_inner1_desc', models.TextField()),
                ('sec1_inner2_title', models.CharField(max_length=100)),
                ('sec1_inner2_desc', models.TextField()),
                ('sec1_inner3_title', models.CharField(max_length=100)),
                ('sec1_inner3_desc', models.TextField()),
                ('sec1_inner4_title', models.CharField(max_length=100)),
                ('sec1_inner4_desc', models.TextField()),
                ('sec2_title', models.CharField(max_length=100)),
                ('sec2_desc', models.TextField()),
                ('sec3_heading', models.CharField(max_length=100)),
                ('sec3_inner1_title', models.CharField(max_length=100)),
                ('sec3_inner1_desc', models.TextField()),
                ('sec3_inner1_value', models.IntegerField()),
                ('sec3_inner2_title', models.CharField(max_length=100)),
                ('sec3_inner2_desc', models.TextField()),
                ('sec3_inner2_value', models.IntegerField()),
                ('sec3_inner3_title', models.CharField(max_length=100)),
                ('sec3_inner3_desc', models.TextField()),
                ('sec3_inner3_value', models.IntegerField()),
                ('sec3_inner4_title', models.CharField(max_length=100)),
                ('sec3_inner4_desc', models.TextField()),
                ('sec3_inner4_value', models.IntegerField()),
                ('sec4_heading', models.CharField(max_length=100)),
                ('sec4_title', models.CharField(max_length=100)),
                ('sec4_inner1_title', models.CharField(max_length=100)),
                ('sec4_inner1_desc', models.TextField()),
                ('sec4_inner2_title', models.CharField(max_length=100)),
                ('sec4_inner2_desc', models.TextField()),
                ('sec4_inner3_title', models.CharField(max_length=100)),
                ('sec4_inner3_desc', models.TextField()),
                ('sec4_inner4_title', models.CharField(max_length=100)),
                ('sec4_inner4_desc', models.TextField()),
                ('sec5_heading', models.CharField(max_length=100)),
                ('sec5_bg_image', models.ImageField(null=True, upload_to='Images/')),
            ],
        ),
        migrations.DeleteModel(
            name='AboutSec1',
        ),
        migrations.DeleteModel(
            name='AboutSec2',
        ),
        migrations.DeleteModel(
            name='AboutSec3',
        ),
        migrations.DeleteModel(
            name='AboutSec4',
        ),
        migrations.DeleteModel(
            name='AboutSec5',
        ),
        migrations.DeleteModel(
            name='AboutSec6',
        ),
        migrations.DeleteModel(
            name='Teamsec1',
        ),
        migrations.DeleteModel(
            name='Teamsec2',
        ),
    ]
