# Generated by Django 3.1.5 on 2021-01-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210116_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='professional_title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('Other', 'O'), ('Full Time', 'F'), ('Part Time', 'P')], max_length=255),
        ),
    ]
