from django.db import models

# Create your models here.


class City(models.Model):
    class CitiesChoice(models.TextChoices):
        ROSSIYA = ('RUS', 'Россия')
        UZBEKISTAN = ('UZB', 'Узбекистан')

    name = models.CharField("Название", max_length=255, blank=True, null=True, db_index=True)
    city = models.CharField('Город', choices=CitiesChoice.choices, default=CitiesChoice.UZBEKISTAN, max_length=255, blank=True, db_index=True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['-pk']

    def __str__(self):
        return f'Страна: {self.city}, Город {self.name}'