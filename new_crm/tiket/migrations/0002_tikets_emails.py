# Generated by Django 3.2.16 on 2022-12-22 16:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('emailing', '0001_initial'),
        ('tiket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tikets',
            name='emails',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='emailing.emails'),
            preserve_default=False,
        ),
    ]
