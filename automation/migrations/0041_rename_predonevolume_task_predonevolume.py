# Generated by Django 4.2.1 on 2023-06-07 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0040_task_predonevolume"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task", old_name="PreDoneVolume", new_name="preDoneVolume",
        ),
    ]
