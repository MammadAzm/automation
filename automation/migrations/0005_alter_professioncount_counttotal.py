# Generated by Django 4.2.1 on 2023-05-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0004_rename_profession_profession_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="professioncount",
            name="countTotal",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
