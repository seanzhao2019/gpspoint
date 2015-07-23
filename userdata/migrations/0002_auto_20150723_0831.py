# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='blood_type',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='destination',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='emergency_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
