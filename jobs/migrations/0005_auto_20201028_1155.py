# Generated by Django 3.1.2 on 2020-10-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20201027_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='bio')),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
