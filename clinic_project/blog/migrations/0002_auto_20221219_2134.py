# Generated by Django 3.2.16 on 2022-12-19 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(db_index=True, default='', max_length=300, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Заголовок'),
        ),
    ]
