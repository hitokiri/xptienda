# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('decoratucasa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 11, 0, 12, 59, 253518, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
