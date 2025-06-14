# Generated by Django 4.2.1 on 2023-08-01 12:11

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0117_alter_dailyreport_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectuser",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=django_jalali.db.models.jDateTimeField(default="1402-05-10 15:41:21"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_created",
            field=django_jalali.db.models.jDateTimeField(default="1402-05-10 15:41:21"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_edited",
            field=django_jalali.db.models.jDateTimeField(default="1402-05-10 15:41:21"),
        ),
    ]
