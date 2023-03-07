# Generated by Django 3.2.16 on 2022-12-26 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icecream_app', '0003_ice_cream_shop_recorder_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ice_cream_shop',
            name='date_of_create',
            field=models.DateField(choices=[(datetime.date(1969, 7, 20), 'Apollo 11 (Eagle)'), (datetime.date(1969, 11, 19), 'Apollo 12 (Intrepid)'), (datetime.date(1971, 2, 5), 'Apollo 13 (Antares)'), (datetime.date(1971, 7, 30), 'Apollo 14 (Falcon)'), (datetime.date(1972, 4, 21), 'Apollo 15 (Orion)'), (datetime.date(1972, 12, 11), 'Apollo 16 (Challenger)')], db_index=True, default=datetime.date(1972, 12, 11), help_text='2022-01-01', verbose_name='Дата Открытия'),
        ),
    ]