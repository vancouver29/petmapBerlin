# Generated by Django 3.0.2 on 2020-01-30 20:31

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land', models.CharField(max_length=7)),
                ('ort', models.CharField(max_length=27)),
                ('result_num', models.CharField(max_length=1)),
                ('osm_id', models.CharField(max_length=10)),
                ('display_na', models.CharField(max_length=151)),
                ('category', models.CharField(max_length=8)),
                ('type', models.CharField(max_length=18)),
                ('latlong', models.CharField(max_length=37)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'animals',
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('gml_id', models.CharField(max_length=80)),
                ('gemeinde_n', models.CharField(max_length=80)),
                ('gemeinde_s', models.CharField(max_length=80)),
                ('land_name', models.CharField(max_length=80)),
                ('land_schlu', models.CharField(max_length=80)),
                ('schluessel', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=254)),
                ('animal_cou', models.CharField(max_length=254)),
                ('district', models.CharField(max_length=254)),
                ('parksize', models.CharField(max_length=254)),
                ('density', models.CharField(max_length=254)),
                ('rent', models.CharField(max_length=254)),
                ('countyid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'counties',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=250, null=True)),
                ('date_reported', models.DateField(auto_now_add=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'locations',
            },
        ),
    ]
