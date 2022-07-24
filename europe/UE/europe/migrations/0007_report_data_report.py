# Generated by Django 4.0.1 on 2022-07-22 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('europe', '0006_remove_report_report_delete_data_report_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('display', models.BooleanField(default=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('menu', models.ForeignKey(limit_choices_to={'group': 'Menu'}, on_delete=django.db.models.deletion.CASCADE, related_name='tag_menu', to='europe.tag')),
                ('submenu', models.ForeignKey(limit_choices_to={'group': 'Submenu'}, on_delete=django.db.models.deletion.CASCADE, related_name='tag_submenu', to='europe.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Data_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2000)),
                ('value', models.IntegerField(default=0)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_data', to='europe.country')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='europe.report')),
            ],
        ),
    ]
