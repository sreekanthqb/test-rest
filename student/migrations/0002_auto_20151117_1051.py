# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_branch_collegecourse'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='studentcollegemap',
            name='year',
        ),
        migrations.AddField(
            model_name='studentcollegemap',
            name='course',
            field=models.ForeignKey(default='', to='college.CollegeCourse'),
            preserve_default=False,
        ),
    ]
