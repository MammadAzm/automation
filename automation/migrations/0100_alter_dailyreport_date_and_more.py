# Generated by Django 4.2.1 on 2023-07-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "automation",
            "0099_remove_taskreport_parenttask_taskreport_operation_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=models.DateTimeField(default="1402-04-20 12:54:21"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_created",
            field=models.DateTimeField(default="1402-04-20 12:54:21"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_edited",
            field=models.DateTimeField(default="1402-04-20 12:54:21"),
        ),
    ]
