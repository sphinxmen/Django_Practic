# Generated by Django 3.2.16 on 2022-12-22 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emailing', '0001_initial'),
        ('tiket', '0002_tikets_emails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tikets',
            name='emails',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='emailing.emails'),
        ),
    ]
