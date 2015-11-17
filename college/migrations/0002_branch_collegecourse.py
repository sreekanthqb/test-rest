# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('course', models.ForeignKey(to='college.Course')),
            ],
        ),
        migrations.CreateModel(
            name='CollegeCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('branch', models.ForeignKey(to='college.Branch')),
                ('college', models.ForeignKey(to='college.College')),
                ('course', models.ForeignKey(to='college.Course')),
            ],
        ),
    ]
