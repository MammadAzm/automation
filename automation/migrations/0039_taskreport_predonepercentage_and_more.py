# Generated by Django 4.2.1 on 2023-06-07 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0038_alter_dailyreport_date_alter_dailyreport_weekday"),
    ]

    operations = [
        migrations.AddField(
            model_name="taskreport",
            name="preDonePercentage",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="taskreport",
            name="preDoneVolume",
            field=models.FloatField(default=0.0),
        ),
    ]
