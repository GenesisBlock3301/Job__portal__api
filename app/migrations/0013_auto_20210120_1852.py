# Generated by Django 3.1.5 on 2021-01-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210117_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'F'), ('Part Time', 'P'), ('Other', 'O')], max_length=255),
        ),
    ]
