# Generated by Django 4.0.1 on 2022-04-09 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('europe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='report',
            name='type_chart',
            field=models.CharField(default='', max_length=255),
        ),
    ]