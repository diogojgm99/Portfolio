# Generated by Django 4.0.1 on 2022-07-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('europe', '0008_rename_sigla_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_report',
            name='value',
            field=models.FloatField(default=0.0),
        ),
    ]
