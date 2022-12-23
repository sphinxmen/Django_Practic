# Generated by Django 3.2.16 on 2022-12-15 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, default='', max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(db_index=True, default='', max_length=100, verbose_name='Фамилия')),
                ('email', models.EmailField(db_index=True, max_length=254, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Режисер',
                'verbose_name_plural': 'Режисеры',
                'ordering': ['first_name'],
            },
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-published_on'], 'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='movies_manager.director'),
        ),
    ]
