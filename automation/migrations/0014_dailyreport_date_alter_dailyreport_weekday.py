# Generated by Django 4.2.1 on 2023-05-28 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0013_dailyreport_weekday"),
    ]

    operations = [
        migrations.AddField(
            model_name="dailyreport",
            name="date",
            field=models.DateField(default="2023-05-28"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="weekday",
            field=models.IntegerField(
                choices=[
                    (1, "دوشنبه"),
                    (2, "سه شنبه"),
                    (3, "چهارشنبه"),
                    (4, "پنج شنبه"),
                    (5, "جمعه"),
                    (6, "شنبه"),
                    (7, "یکشنبه"),
                ],
                default=6,
            ),
        ),
    ]
