# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 14:33
from __future__ import unicode_literals

from django.db import migrations, models

import openslides.utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0006_require_contenttypes_0002"),
        # The next line is not a dependency because we also want to support Django 1.8.
        # ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("username", models.CharField(blank=True, max_length=255, unique=True)),
                ("first_name", models.CharField(blank=True, max_length=255)),
                ("last_name", models.CharField(blank=True, max_length=255)),
                (
                    "structure_level",
                    models.CharField(blank=True, default="", max_length=255),
                ),
                ("title", models.CharField(blank=True, default="", max_length=50)),
                ("about_me", models.TextField(blank=True, default="")),
                ("comment", models.TextField(blank=True, default="")),
                (
                    "default_password",
                    models.CharField(blank=True, default="", max_length=100),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_present", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "permissions": (
                    ("can_see_name", "Can see names of users"),
                    (
                        "can_see_extra_data",
                        "Can see extra data of users (e.g. present and comment)",
                    ),
                    ("can_manage", "Can manage users"),
                ),
                "default_permissions": (),
                "ordering": ("last_name", "first_name", "username"),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        )
    ]
