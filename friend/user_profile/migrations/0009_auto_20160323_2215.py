# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_auto_20160323_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberprofile',
            name='users',
        ),
        migrations.AddField(
            model_name='memberprofile',
            name='users',
            field=models.ManyToManyField(to='user_profile.UserProfile'),
        ),
    ]
