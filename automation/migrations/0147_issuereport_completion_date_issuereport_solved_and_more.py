# Generated by Django 4.2.1 on 2023-08-10 10:01

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0146_alter_dailyreport_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="issuereport",
            name="completion_date",
            field=django_jalali.db.models.jDateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="issuereport",
            name="solved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="issuereport",
            name="start_date",
            field=django_jalali.db.models.jDateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=django_jalali.db.models.jDateTimeField(default="1402-05-19 13:31:06"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_created",
            field=django_jalali.db.models.jDateTimeField(default="1402-05-19 13:31:06"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_edited",
            field=django_jalali.db.models.jDateTimeField(default="1402-05-19 13:31:06"),
        ),
        migrations.CreateModel(
            name="IssueCount",
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
                    "dailyReport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.dailyreport",
                    ),
                ),
                (
                    "issue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.issuereport",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="automation.project",
                    ),
                ),
            ],
            options={"unique_together": {("dailyReport", "project", "issue")},},
        ),
        migrations.AddField(
            model_name="dailyreport",
            name="issues",
            field=models.ManyToManyField(
                through="automation.IssueCount", to="automation.issuereport"
            ),
        ),
    ]
