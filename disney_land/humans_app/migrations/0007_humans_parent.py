# Generated by Django 3.2.16 on 2022-12-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humans_app', '0006_alter_humans_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='humans',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=models.SET(1), to='humans_app.child'),
        ),
    ]