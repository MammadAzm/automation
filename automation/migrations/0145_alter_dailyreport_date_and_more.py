# Generated by Django 4.2.1 on 2023-08-10 09:36

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0144_machinecount_onrent_alter_dailyreport_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=django_jalali.db.models.jDateTimeField(default="1402-05-19 13:06:02"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_created",
            field=django_jalali.db.models.jDateTimeField(default="1402-05-19 13:06:02"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_edited",
            field=django_jalali.db.models.jDateTimeField(default="1402-05-19 13:06:02"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="short_date",
            field=django_jalali.db.models.jDateField(default="1402-05-19"),
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
                default=5,
            ),
        ),
        migrations.CreateModel(
            name="Issue",
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
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.project",
                    ),
                ),
            ],
            options={"unique_together": {("name", "project")},},
        ),
    ]
