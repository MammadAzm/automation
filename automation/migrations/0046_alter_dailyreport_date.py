# Generated by Django 4.2.1 on 2023-06-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0045_dailyreport_deletable"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=models.DateField(default="1402-03-17:17-21-42"),
        ),
    ]
