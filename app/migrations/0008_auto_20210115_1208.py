# Generated by Django 3.1.5 on 2021-01-15 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210115_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'F'), ('Part Time', 'P'), ('Other', 'O')], max_length=255),
        ),
    ]
