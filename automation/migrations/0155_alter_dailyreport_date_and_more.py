# Generated by Django 4.2.1 on 2023-08-20 10:55

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0154_project_temp_code_alter_dailyreport_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyreport",
            name="date",
            field=django_jalali.db.models.jDateTimeField(default="1402-05-29 14:25:22"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_created",
            field=django_jalali.db.models.jDateTimeField(default="1402-05-29 14:25:22"),
        ),
        migrations.AlterField(
            model_name="dailyreport",
            name="date_edited",
            field=django_jalali.db.models.jDateTimeField(default="1402-05-29 14:25:22"),
        ),
        migrations.AlterField(
            model_name="equipe",
            name="name",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
