# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('user_id', models.IntegerField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('blood_type', models.CharField(max_length=6)),
                ('emergency_number', models.IntegerField()),
                ('destination', models.CharField(max_length=20)),
            ],
        ),
    ]
