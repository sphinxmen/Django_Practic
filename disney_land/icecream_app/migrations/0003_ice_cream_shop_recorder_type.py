# Generated by Django 3.2.16 on 2022-12-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icecream_app', '0002_auto_20221226_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='ice_cream_shop',
            name='recorder_type',
            field=models.CharField(blank=True, choices=[('Audio', (('viny1', 'Viny2'), ('cd', 'CD'))), ('Video', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))), ('unknown', 'Unknown')], max_length=250, verbose_name='Тип проигравателя'),
        ),
    ]
