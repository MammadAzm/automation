# Generated by Django 4.2.1 on 2023-06-05 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("automation", "0034_alter_task_unique_together_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="unique_str",
            field=models.CharField(default="A", max_length=250),
            preserve_default=False,
        ),
    ]
