# Generated by Django 3.1.5 on 2021-01-15 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210111_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'F'), ('Other', 'O'), ('Part Time', 'P')], max_length=255),
        ),
    ]
