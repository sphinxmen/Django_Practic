from django.db import models
import datetime
from cities_app.models import City

# Create your models here.

MEDIA_CHOICES = [
    ('Audio', (
        ('viny1', 'Viny2'),
        ('cd', 'CD')
    )
     ),
    ('Video', (
        ('vhs', 'VHS Tape'),
        ('dvd', 'DVD')
    )
     ),
    ('unknown', 'Unknown')
]



class Ice_cream(models.Model):
    name = models.CharField('name', default='', max_length=100, null=False, db_index=True,
                            help_text='Клубничка')
    sort_of = models.CharField('sort_of', default='', null=False, max_length=100, db_index=True, help_text='Пломбир')
    price = models.FloatField('price', default='', max_length=100, null=False, db_index=True)

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'
        ordering = ['-pk']

    def __str__(self):
        return f'name: {self.name} sort_of:{self.sort_of} price:{self.price}'


class Ice_cream_shop(models.Model):

    class IceCreameShopChoices(datetime.date, models.Choices):
        APOLLO_11  =1969, 7, 20, 'Apollo 11 (Eagle)'
        APOLLO_12  =1969, 11, 19, 'Apollo 12 (Intrepid)'
        APOLLO_13  =1971, 2, 5, 'Apollo 13 (Antares)'
        APOLLO_14  =1971, 7, 30, 'Apollo 14 (Falcon)'
        APOLLO_15  =1972, 4, 21, 'Apollo 15 (Orion)'
        APOLLO_16  =1972, 12, 11, 'Apollo 16 (Challenger)'

    # date_of_create = models.DateField('Date', default='', max_length=100, null=False, db_index=True,
    date_of_create = models.DateField('Дата Открытия', default=IceCreameShopChoices.APOLLO_16, db_index=True, choices=IceCreameShopChoices.choices,
                                      help_text='2022-01-01')
    address = models.CharField('address', default='', max_length=100, null=False, db_index=True,
                               help_text='ул. Ленина, 12')
    name = models.CharField('name', default='', max_length=100, null=False, db_index=True, help_text='Чебурашка')
    ower = models.CharField('ower', default='', max_length=100, null=False, db_index=True, help_text='Белый Хозяин')
    geo = models.CharField('geo', default='', max_length=100, null=False, db_index=True,
                           help_text='48.1212121, 68.565656')
    recorder_type = models.CharField('Тип проигравателя', choices=MEDIA_CHOICES, max_length=250, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Киоск'
        verbose_name_plural = 'Киоски'
        ordering = ['-pk']

    def __str__(self):
        return f'date_of_create: {self.date_of_create} address:{self.address} name:{self.name}'
