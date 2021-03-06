# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_userprofile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'ritu')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.AddField(
            model_name='memberprofile',
            name='users',
            field=models.ForeignKey(to='user_profile.UserProfile'),
        ),
    ]
