# Generated by Django 3.2.16 on 2022-12-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icecream_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ice_cream_shop',
            name='address',
            field=models.CharField(db_index=True, default='', help_text='ул. Ленина, 12', max_length=100, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='ice_cream_shop',
            name='geo',
            field=models.CharField(db_index=True, default='', help_text='48.1212121, 68.565656', max_length=100, verbose_name='geo'),
        ),
        migrations.AlterField(
            model_name='ice_cream_shop',
            name='name',
            field=models.CharField(db_index=True, default='', help_text='Чебурашка', max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='ice_cream_shop',
            name='ower',
            field=models.CharField(db_index=True, default='', help_text='Белый Хозяин', max_length=100, verbose_name='ower'),
        ),
    ]
