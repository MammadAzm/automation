# Generated by Django 4.2.1 on 2023-06-05 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0032_zone_alter_machine_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("name", models.CharField(max_length=250)),
                ("totalVolume", models.FloatField(default=0.1)),
                ("doneVolume", models.FloatField(default=0.0)),
                ("donePercentage", models.FloatField(default=0.0)),
                (
                    "equipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.equipe",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.unit",
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
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=models.DateField(default="1402-03-15"),
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
                default=2,
            ),
        ),
        migrations.CreateModel(
            name="TaskReport",
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
                ("todayVolume", models.FloatField(default=0.0)),
                (
                    "dailyReport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.dailyreport",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.task",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="dailyreport",
            name="tasks",
            field=models.ManyToManyField(
                through="automation.TaskReport", to="automation.task"
            ),
        ),
    ]
