# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-11-19 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_head'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='gender',
            field=models.CharField(choices=[('other', 'other'), ('male', 'male'), ('female', 'female')], max_length=50),
        ),
        migrations.AlterField(
            model_name='parent',
            name='relation',
            field=models.CharField(choices=[('father', 'father'), ('mother', 'mother'), ('guardian', 'guardian')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='division',
            field=models.CharField(choices=[('BE1', 'BE1'), ('FE1', 'FE1'), ('TE1', 'TE1'), ('SE1', 'SE1')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('other', 'other'), ('male', 'male'), ('female', 'female')], max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='division',
            field=models.CharField(choices=[('BE1', 'BE1'), ('FE1', 'FE1'), ('TE1', 'TE1'), ('SE1', 'SE1')], max_length=50),
        ),
    ]
