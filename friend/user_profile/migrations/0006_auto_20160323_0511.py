# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_memberprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberprofile',
            name='member',
        ),
        migrations.DeleteModel(
            name='MemberProfile',
        ),
    ]
