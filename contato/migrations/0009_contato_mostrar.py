# Generated by Django 2.2.15 on 2020-08-07 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0008_auto_20200806_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]