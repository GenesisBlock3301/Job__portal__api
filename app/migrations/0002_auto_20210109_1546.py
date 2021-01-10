# Generated by Django 3.1.5 on 2021-01-09 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_cats', to='app.category'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('Other', 'O'), ('Part Time', 'P'), ('Full Time', 'F')], max_length=255),
        ),
    ]