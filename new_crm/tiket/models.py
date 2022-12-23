from django.db import models
from emailing.models import Emails

# Create your models here.

class Tikets(models.Model):
    emails = models.ForeignKey(Emails, on_delete=models.CASCADE, blank=True)
    number = models.IntegerField('number', default='', null=False, db_index=True)
    date_create = models.DateTimeField('date_create', default='', null=False, db_index=True)
    date_update = models.DateTimeField('date_update', default='', null=False, db_index=True)

    class Meta:
        verbose_name = 'Tiket'
        verbose_name_plural = 'Tikets'
        ordering = ['-pk']

    def __str__(self):
        return f'номер: {self.number} дата создания:{self.date_create} дата обновления:{self.date_update}'