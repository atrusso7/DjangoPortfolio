# Generated by Django 3.1.2 on 2020-10-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(default='company', max_length=100),
        ),
        migrations.AddField(
            model_name='job',
            name='job_title',
            field=models.CharField(default='title', max_length=100),
        ),
    ]