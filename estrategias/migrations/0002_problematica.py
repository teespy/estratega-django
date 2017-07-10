# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estrategias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problematica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('texto', models.TextField()),
                ('estrategia', models.ForeignKey(to='estrategias.Estrategia')),
            ],
        ),
    ]
