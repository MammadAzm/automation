# Generated by Django 4.2.1 on 2023-07-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0087_alter_dailyreport_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="operation",
            name="zones",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="zones",
                to="automation.zoneoperation",
            ),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=models.DateTimeField(default="1402-04-16 12:21:01"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_created",
            field=models.DateTimeField(default="1402-04-16 12:21:01"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_edited",
            field=models.DateTimeField(default="1402-04-16 12:21:01"),
        ),
    ]
