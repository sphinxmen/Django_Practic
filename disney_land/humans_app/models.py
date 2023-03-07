from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
import re
from.validators import validate_address_lenght

# Create your models here.

CENDER = [
    (None, "Не определено"),
    (1, "Мужчина"),
    (0, "Женшина"),
]

class BasePerson(models.Model):
    class PersonGenderChoice(models.IntegerChoices):
        MALE = 1, _("Мужчина")
        FEMALE = 0, _("Женщина")
        __empty__ = _("Не определенно")

    name = models.CharField("Имя", max_length=255, blank=True, null=True, validators=[RegexValidator(regex='^\D+$',message='Введите строку', flags=re.IGNORECASE)])
    age = models.IntegerField("Вазраст", default=1, blank=True, null=True)
    gender = models.BooleanField("Пол", default=PersonGenderChoice.MALE, choices=PersonGenderChoice.choices, blank=True,
                                 null=True)
    address = models.CharField("Адрес", max_length=255, blank=True, null=True, validators=[validate_address_lenght])

    class Meta:
        abstract = True

    def gender_p(self):
        sub_class = self.__class__.__name__
        if sub_class == "Humans":
            if self.gender == 1:
                return "Мужчина"
            else:
                return "Женщина"
        elif sub_class == 'Child':
            if self.gender == 1:
                return "Мальчик"
            else:
                return "Девочка"



    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender_p()}'

    def save(self,*args,**kwargs):
        if self.name == 'Irod':
            return
        else:
            super().save(*args, **kwargs)


class Humans(BasePerson):
    NAME_TERMS_CHOICES = [
        ('Blasic', (
            ('mr', 'Mr'),
            ('ms', 'Ms'),
        )
         ),
        ('Prof',(
            ('dr', 'Dr'),
            ('sir', 'Sir'),
        )
         ),
        ('unknown', 'Unknown'),
    ]
    name_terms = models.CharField("Обращение", default=NAME_TERMS_CHOICES[1][1], choices=NAME_TERMS_CHOICES, max_length=255)

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['-pk']
        get_latest_by = ['-age']

        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=16), name='age'),
        ]

    def get_absolute_url(self):
        return f'/human/person/{self.pk}'


class Child(BasePerson):
    parent_field = models.ManyToManyField(Humans, through='PersonRelationShip')
    age = models.IntegerField("Возраст", default=1, blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(15)])


class PersonRelationShip(models.Model):
    parent = models.ForeignKey(Humans, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

    def __str__(self):
        return f'Родители: {self.parent} - Ребенок: {self.child}'

    class Meta:
        verbose_name = 'Отнашения'
        verbose_name_plural = 'Отнашения'
        unique_together = ['child']
