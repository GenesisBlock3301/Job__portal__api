# Generated by Django 3.1.5 on 2021-01-15 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210115_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('Part Time', 'P'), ('Other', 'O'), ('Full Time', 'F')], max_length=255),
        ),
    ]
