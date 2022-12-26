# Generated by Django 4.0.7 on 2022-11-22 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone_no',
        ),
        migrations.AddField(
            model_name='patient',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 22, 14, 32, 22, 737958)),
        ),
        migrations.AddField(
            model_name='patient',
            name='message',
            field=models.TextField(default=''),
        ),
    ]