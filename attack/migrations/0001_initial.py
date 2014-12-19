# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attacker_ip', models.IPAddressField()),
                ('service_name', models.CharField(max_length=140)),
                ('protocol', models.CharField(max_length=140)),
                ('port', models.CharField(max_length=140)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('country_name', models.CharField(max_length=255)),
                ('geo_location', models.CharField(max_length=140)),
                ('timestamp', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
