# Generated by Django 4.2.1 on 2023-06-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0052_dailyreport_temperature_max_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="dailyreport",
            name="weather",
            field=models.IntegerField(
                choices=[
                    (0, "تعیین نشده"),
                    (1, "آفتابی"),
                    (2, "ابری"),
                    (3, "بارانی"),
                    (4, "برفی"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=models.DateTimeField(default="1402-03-18 13:00:49"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_created",
            field=models.DateTimeField(default="1402-03-18 13:00:49"),
        ),
    ]
