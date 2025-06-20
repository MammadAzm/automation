# Generated by Django 4.2.1 on 2023-08-26 07:31

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0158_issuecount_state_alter_dailyreport_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=django_jalali.db.models.jDateTimeField(default="1402-06-04 11:01:05"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_created",
            field=django_jalali.db.models.jDateTimeField(default="1402-06-04 11:01:05"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_edited",
            field=django_jalali.db.models.jDateTimeField(default="1402-06-04 11:01:05"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="short_date",
            field=django_jalali.db.models.jDateField(default="1402-06-04"),
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
                default=0,
            ),
        ),
    ]
