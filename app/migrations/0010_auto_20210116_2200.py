# Generated by Django 3.1.5 on 2021-01-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210116_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('Other', 'O'), ('Part Time', 'P'), ('Full Time', 'F')], max_length=255),
        ),
    ]