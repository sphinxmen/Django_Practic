from django.db import models

# Create your models here.

class Emails(models.Model):

    number = models.IntegerField('number',  default='', null=False, db_index=True)
    date_create = models.DateTimeField('date_create', default='', null=False, db_index=True)
    to_email = models.CharField('to_email', max_length=100, default='', null=False, db_index=True)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'
        ordering = ['-pk']

    def __str__(self):
        return f'номер: {self.number} дата создания:{self.date_create} to_email:{self.to_email}'