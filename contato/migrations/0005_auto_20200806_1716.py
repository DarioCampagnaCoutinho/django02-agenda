# Generated by Django 2.2.15 on 2020-08-06 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0004_auto_20200806_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]