# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20150723_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
