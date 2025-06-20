# Generated by Django 4.2.1 on 2023-07-05 11:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0069_alter_dailyreport_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Operation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, unique=True)),
                ("amount", models.FloatField(default=0.0)),
                ("assignedAmount", models.FloatField(default=0.0)),
                ("doneAmount", models.FloatField(default=0.0)),
                ("fullyAssigned", models.BooleanField(default=False)),
                ("fullyDone", models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=models.DateTimeField(default="1402-04-14 15:20:39"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_created",
            field=models.DateTimeField(default="1402-04-14 15:20:39"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_edited",
            field=models.DateTimeField(default="1402-04-14 15:20:39"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="short_date",
            field=models.DateField(default="1402-04-14"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="weekday",
            field=models.IntegerField(
                choices=[
                    (2, "دوشنبه"),
                    (3, "سه شنبه"),
                    (4, "چهارشنبه"),
                    (5, "پنج شنبه"),
                    (6, "جمعه"),
                    (0, "شنبه"),
                    (1, "یکشنبه"),
                ],
                default=4,
            ),
        ),
        migrations.CreateModel(
            name="SubOperation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "weight",
                    models.FloatField(
                        default=0.0,
                        validators=[
                            django.core.validators.MinValueValidator(0.0),
                            django.core.validators.MaxValueValidator(100.0),
                        ],
                    ),
                ),
                ("amount", models.FloatField(default=0.0)),
                ("doneAmount", models.FloatField(default=0.0)),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.operation",
                    ),
                ),
                (
                    "parentplussubs",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="AA",
                        to="automation.operation",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.unit",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OperationBreak",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.FloatField(default=0.0)),
                ("doneAmount", models.FloatField(default=0.0)),
                (
                    "operation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.operation",
                    ),
                ),
                (
                    "zone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.zone",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="operation",
            name="suboperations",
            field=models.ManyToManyField(
                related_name="operations", to="automation.suboperation"
            ),
        ),
        migrations.AddField(
            model_name="operation",
            name="unit",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="operation_unit",
                to="automation.unit",
            ),
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.FloatField(default=0.0)),
                ("doneAmount", models.FloatField(default=0.0)),
                (
                    "operation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.operationbreak",
                    ),
                ),
                (
                    "suboperation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.suboperation",
                    ),
                ),
            ],
        ),
    ]
