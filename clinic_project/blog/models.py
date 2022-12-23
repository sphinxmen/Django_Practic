from django.db import models

# Create your models here.

class Article(models.Model):

    title = models.CharField('Заголовок', max_length=200, default='', null=False, db_index=True)
    content = models.TextField('Содержание', max_length=300, default='', null=False, db_index=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-pk']

    def __str__(self):
        return f'{self.title} {self.content}'