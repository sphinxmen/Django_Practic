# Generated by Django 3.2.16 on 2022-12-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(db_index=True, default='', verbose_name='number')),
                ('date_create', models.DateTimeField(db_index=True, default='', verbose_name='date_create')),
                ('to_email', models.CharField(db_index=True, default='', max_length=100, verbose_name='to_email')),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
                'ordering': ['-pk'],
            },
        ),
    ]
