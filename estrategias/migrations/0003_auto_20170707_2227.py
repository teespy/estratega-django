# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estrategias', '0002_problematica'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActorRelevante',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('justificacion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Barrera',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Causa',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('texto', models.TextField()),
                ('estrategia', models.ForeignKey(to='estrategias.Estrategia')),
            ],
        ),
        migrations.CreateModel(
            name='FactorHabilitante',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('texto', models.TextField()),
                ('estrategia', models.ForeignKey(to='estrategias.Estrategia')),
            ],
        ),
        migrations.CreateModel(
            name='ResultadoIntermedio',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('texto', models.TextField()),
                ('objetivo', models.ForeignKey(to='estrategias.Objetivo')),
            ],
        ),
        migrations.CreateModel(
            name='SolucionPolitica',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('texto', models.TextField()),
                ('estrategia', models.ForeignKey(to='estrategias.Estrategia')),
            ],
        ),
        migrations.AddField(
            model_name='factorhabilitante',
            name='objetivo',
            field=models.ForeignKey(to='estrategias.Objetivo'),
        ),
        migrations.AddField(
            model_name='barrera',
            name='objetivo',
            field=models.ForeignKey(to='estrategias.Objetivo'),
        ),
        migrations.AddField(
            model_name='actorrelevante',
            name='objetivo',
            field=models.ForeignKey(to='estrategias.Objetivo'),
        ),
    ]
