# Generated by Django 2.2.15 on 2020-08-06 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0002_auto_20200806_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(),
        ),
    ]