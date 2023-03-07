# Generated by Django 3.2.16 on 2022-12-26 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humans_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humans',
            name='gender',
            field=models.BooleanField(blank=True, choices=[(1, 'Мужчина'), (0, 'Женшина')], db_index=True, default='1', verbose_name='gender'),
        ),
    ]