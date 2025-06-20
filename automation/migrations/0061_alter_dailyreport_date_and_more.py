# Generated by Django 4.2.1 on 2023-06-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0060_machinecount_workhours_alter_dailyreport_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=models.DateTimeField(default="1402-03-28 00:15:10"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_created",
            field=models.DateTimeField(default="1402-03-28 00:15:10"),
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
        migrations.AlterField(
            model_name="machinecount",
            name="workHours",
            field=models.PositiveIntegerField(default=0.0),
        ),
    ]
