# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("mediafiles", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="mediafile",
            options={
                "default_permissions": (),
                "ordering": ["title"],
                "permissions": (
                    ("can_see", "Can see the list of files"),
                    ("can_see_hidden", "Can see hidden files"),
                    ("can_upload", "Can upload files"),
                    ("can_manage", "Can manage files"),
                ),
            },
        ),
        migrations.AddField(
            model_name="mediafile",
            name="hidden",
            field=models.BooleanField(default=False),
        ),
    ]
