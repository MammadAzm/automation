# Generated by Django 4.2.1 on 2023-06-26 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0067_alter_dailyreport_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=models.DateTimeField(default="1402-04-05 13:33:35"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_created",
            field=models.DateTimeField(default="1402-04-05 13:33:35"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_edited",
            field=models.DateTimeField(default="1402-04-05 13:33:35"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="short_date",
            field=models.DateField(default="1402-04-05"),
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
        migrations.AlterUniqueTogether(
            name="machinecount",
            unique_together={("dailyReport", "machine", "provider")},
        ),
        migrations.AlterUniqueTogether(
            name="materialcount",
            unique_together={("dailyReport", "material", "provider")},
        ),
    ]
