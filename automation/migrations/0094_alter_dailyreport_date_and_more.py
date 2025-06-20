# Generated by Django 4.2.1 on 2023-07-09 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0093_zoneoperation_tasks_alter_dailyreport_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=models.DateTimeField(default="1402-04-18 12:24:06"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_created",
            field=models.DateTimeField(default="1402-04-18 12:24:06"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_edited",
            field=models.DateTimeField(default="1402-04-18 12:24:06"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="short_date",
            field=models.DateField(default="1402-04-18"),
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
                default=1,
            ),
        ),
        migrations.CreateModel(
            name="ParentTask",
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
                ("unique_str", models.CharField(max_length=250, unique=True)),
                ("totalVolume", models.FloatField(default=0.1)),
                ("doneVolume", models.FloatField(default=0.0)),
                ("donePercentage", models.FloatField(default=0.0)),
                ("started", models.BooleanField(default=False)),
                ("completed", models.BooleanField(default=False)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("completion_date", models.DateField(blank=True, null=True)),
                (
                    "equipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.equipe",
                    ),
                ),
                (
                    "operation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.zoneoperation",
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
            options={"unique_together": {("operation", "equipe", "zone")},},
        ),
        migrations.AddField(
            model_name="task",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="automation.parenttask",
            ),
        ),
    ]
