# Generated by Django 2.2.15 on 2020-08-06 20:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0005_auto_20200806_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 20, 20, 17, 141101, tzinfo=utc)),
        ),
    ]
