# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import decoratucasa.models


class Migration(migrations.Migration):

    dependencies = [
        ('decoratucasa', '0002_auto_20141120_0233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boletin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(upload_to=decoratucasa.models.nombre_modificar)),
                ('descripcion', models.TextField(max_length=900)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Boletin',
                'verbose_name_plural': 'Boletines',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(max_length=900)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('fecha_inicio', models.DateField(auto_now_add=True)),
                ('fecha_final', models.DateField()),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producto', models.CharField(max_length=50)),
                ('precio', models.DecimalField(max_digits=5, decimal_places=2)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('fecha_inicio', models.DateField(auto_now=True)),
                ('fecha_final', models.DateField()),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Ofertas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Suscriptor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activo', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Suscriptor',
                'verbose_name_plural': 'Suscriptores',
            },
            bases=(models.Model,),
        ),
    ]
