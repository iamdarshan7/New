# Generated by Django 2.2.17 on 2020-11-25 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_page', '0020_aboutsec4_sec4_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec1_title', models.CharField(max_length=100)),
                ('sec1_image', models.ImageField(upload_to='Images/')),
                ('sec2_title', models.CharField(max_length=100, null=True)),
                ('sec2_desc', models.TextField(blank=True)),
                ('sec2_dynamic_image', models.ImageField(null=True, upload_to='Images/')),
                ('sec2_dynamic_title', models.CharField(max_length=100)),
                ('sec2_dynamic_desc', models.TextField()),
                ('sec2_dynamic_icon_choice', models.CharField(choices=[('computer', 'computer'), ('support', 'support'), ('process', 'process'), ('development', 'development')], max_length=11)),
                ('sec3_title', models.CharField(max_length=100, null=True)),
                ('sec3_desc', models.TextField(blank=True)),
                ('sec3_dynamic_title', models.CharField(max_length=100)),
                ('sec3_dynamic_desc', models.TextField()),
                ('sec3_dynamic_image', models.ImageField(upload_to='Images/')),
                ('sec4_title', models.CharField(max_length=100, null=True)),
                ('sec4_image', models.ImageField(null=True, upload_to='')),
                ('sec4_dynamic_value', models.IntegerField()),
                ('sec4_dynamic_title', models.CharField(max_length=100)),
                ('sec4_dynamic_desc', models.TextField()),
                ('sec4_dynamic_image', models.ImageField(null=True, upload_to='Images/')),
                ('sec5_title', models.CharField(max_length=100, null=True)),
                ('sec5_desc', models.TextField(blank=True)),
                ('sec5_dynamic_desc', models.TextField()),
                ('sec5_dynamic_title', models.CharField(max_length=100)),
                ('sec5_dynamic_image', models.ImageField(null=True, upload_to='Images/')),
                ('sec6_title', models.CharField(max_length=100, null=True)),
                ('sec6_dynamic_image', models.ImageField(upload_to='Images/')),
                ('sec6_dynamic_desc', models.TextField(blank=True)),
                ('sec6_dynamic_name_person', models.CharField(max_length=100)),
                ('sec6_dynamic_profession', models.CharField(max_length=100)),
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
        migrations.AlterField(
            model_name='teamsec2',
            name='sec2_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
