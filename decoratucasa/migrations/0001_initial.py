# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import decoratucasa.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriasProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'CategoriasProducto',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(max_digits=5, decimal_places=2)),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField(max_length=900)),
                ('imagen', models.ImageField(upload_to=decoratucasa.models.nombre_modificar)),
                ('categoria_s', models.ManyToManyField(to='decoratucasa.CategoriasProducto')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
            bases=(models.Model,),
        ),
    ]
