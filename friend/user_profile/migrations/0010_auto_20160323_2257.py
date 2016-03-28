# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0009_auto_20160323_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberprofile',
            name='users',
        ),
        migrations.AddField(
            model_name='memberprofile',
            name='users',
            field=models.ForeignKey(to='user_profile.UserProfile', null=True),
        ),
    ]
