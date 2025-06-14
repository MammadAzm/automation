# Generated by Django 4.2.1 on 2023-06-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0061_alter_dailyreport_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="completion_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="task",
            name="start_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="task", name="started", field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=models.DateTimeField(default="1402-03-30 11:05:22"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_created",
            field=models.DateTimeField(default="1402-03-30 11:05:22"),
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
                default=3,
            ),
        ),
    ]
