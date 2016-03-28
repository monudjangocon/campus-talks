# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20160322_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=1, choices=[(b'Male', b'M'), (b'Female', b'F'), (b'Not Sure', b'Nd')])),
                ('address', models.TextField()),
                ('image', models.ImageField(upload_to=b'ritu')),
                ('member', models.ForeignKey(to='user_profile.UserProfile')),
            ],
        ),
    ]
