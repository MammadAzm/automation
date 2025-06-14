# Generated by Django 4.2.1 on 2023-07-05 15:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0082_alter_dailyreport_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=models.DateTimeField(default="1402-04-14 19:09:48"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_created",
            field=models.DateTimeField(default="1402-04-14 19:09:48"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_edited",
            field=models.DateTimeField(default="1402-04-14 19:09:48"),
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
                ("name", models.CharField(max_length=250, unique=True)),
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
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.unit",
                    ),
                ),
            ],
            options={"unique_together": {("name", "parent")},},
        ),
    ]
