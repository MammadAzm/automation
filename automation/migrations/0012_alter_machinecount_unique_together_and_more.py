# Generated by Django 4.2.1 on 2023-05-28 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0011_dailyreport_countmachines_dailyreport_machines_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="machinecount", unique_together={("dailyReport", "machine")},
        ),
        migrations.AlterUniqueTogether(
            name="positioncount", unique_together={("dailyReport", "position")},
        ),
        migrations.AlterUniqueTogether(
            name="professioncount", unique_together={("dailyReport", "profession")},
        ),
    ]
