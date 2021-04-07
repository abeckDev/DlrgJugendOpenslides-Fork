# Generated by Django 2.2.6 on 2019-10-17 08:40

from decimal import Decimal

import django.core.validators
from django.conf import settings
from django.db import migrations, models

import openslides.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0011_postgresql_auth_group_id_sequence"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("assignments", "0007_assignment_attachments"),
    ]

    operations = [
        migrations.RenameField(
            model_name="assignmentoption", old_name="candidate", new_name="user"
        ),
        migrations.AddField(
            model_name="assignmentpoll",
            name="global_abstain",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="assignmentpoll",
            name="global_no",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="assignmentpoll",
            name="db_amount_global_abstain",
            field=models.DecimalField(
                blank=True,
                decimal_places=6,
                max_digits=15,
                null=True,
                validators=[django.core.validators.MinValueValidator(Decimal("-2"))],
            ),
        ),
        migrations.AddField(
            model_name="assignmentpoll",
            name="db_amount_global_no",
            field=models.DecimalField(
                blank=True,
                decimal_places=6,
                max_digits=15,
                null=True,
                validators=[django.core.validators.MinValueValidator(Decimal("-2"))],
            ),
        ),
        migrations.AddField(
            model_name="assignmentpoll",
            name="groups",
            field=models.ManyToManyField(blank=True, to="users.Group"),
        ),
        migrations.AddField(
            model_name="assignmentpoll",
            name="state",
            field=models.IntegerField(
                choices=[
                    (1, "Created"),
                    (2, "Started"),
                    (3, "Finished"),
                    (4, "Published"),
                ],
                default=1,
            ),
        ),
        migrations.AddField(
            model_name="assignmentpoll",
            name="title",
            field=models.CharField(default="Poll", max_length=255, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="assignmentpoll",
            name="type",
            field=models.CharField(
                choices=[
                    ("analog", "Analog"),
                    ("named", "Named"),
                    ("pseudoanonymous", "Pseudoanonymous"),
                ],
                default="analog",
                max_length=64,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="assignmentpoll",
            name="votes_amount",
            field=models.IntegerField(
                default=1, validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AddField(
            model_name="assignmentpoll",
            name="voted",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="assignmentvote",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=openslides.utils.models.SET_NULL_AND_AUTOUPDATE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="assignmentpoll",
            name="allow_multiple_votes_per_candidate",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="assignmentpoll",
            name="majority_method",
            field=models.CharField(
                choices=[
                    ("simple", "Simple majority"),
                    ("two_thirds", "Two-thirds majority"),
                    ("three_quarters", "Three-quarters majority"),
                    ("disabled", "Disabled"),
                ],
                default="",
                max_length=14,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="assignmentpoll",
            name="onehundred_percent_base",
            field=models.CharField(
                choices=[
                    ("YN", "Yes/No per candidate"),
                    ("YNA", "Yes/No/Abstain per candidate"),
                    ("votes", "Sum of votes including general No/Abstain"),
                    ("valid", "All valid ballots"),
                    ("cast", "All casted ballots"),
                    ("disabled", "Disabled (no percents)"),
                ],
                default="",
                max_length=8,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="assignment",
            name="number_poll_candidates",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="assignment",
            name="poll_description_default",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="assignmentoption",
            name="poll",
            field=models.ForeignKey(
                on_delete=openslides.utils.models.CASCADE_AND_AUTOUPDATE,
                related_name="options",
                to="assignments.AssignmentPoll",
            ),
        ),
        migrations.AlterField(
            model_name="assignmentvote",
            name="option",
            field=models.ForeignKey(
                on_delete=openslides.utils.models.CASCADE_AND_AUTOUPDATE,
                related_name="votes",
                to="assignments.AssignmentOption",
            ),
        ),
        migrations.RenameField(
            model_name="assignment",
            old_name="poll_description_default",
            new_name="default_poll_description",
        ),
        migrations.AlterField(
            model_name="assignmentpoll",
            name="description",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="assignmentpoll",
            name="pollmethod",
            field=models.CharField(
                choices=[
                    ("votes", "Yes per candidate"),
                    ("YN", "Yes/No per candidate"),
                    ("YNA", "Yes/No/Abstain per candidate"),
                ],
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="assignmentvote",
            name="weight",
            field=models.DecimalField(
                decimal_places=6,
                default=Decimal("1"),
                max_digits=15,
                validators=[django.core.validators.MinValueValidator(Decimal("-2"))],
            ),
        ),
        migrations.AlterField(
            model_name="assignmentpoll",
            name="assignment",
            field=models.ForeignKey(
                on_delete=openslides.utils.models.CASCADE_AND_AUTOUPDATE,
                related_name="polls",
                to="assignments.Assignment",
            ),
        ),
        migrations.RenameField(
            model_name="assignmentpoll", old_name="votescast", new_name="db_votescast"
        ),
        migrations.RenameField(
            model_name="assignmentpoll",
            old_name="votesinvalid",
            new_name="db_votesinvalid",
        ),
        migrations.RenameField(
            model_name="assignmentpoll", old_name="votesvalid", new_name="db_votesvalid"
        ),
    ]
