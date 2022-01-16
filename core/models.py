from django.db import models
from django.contrib.auth.models import User

#
class Job(models.Model):
    """
    Рабочее место
    """

    name = models.CharField(
        verbose_name='Название',
        max_length=256,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = u'рабочее место'
        verbose_name_plural = u'Рабочие места'

    def __str__(self):
        return self.name


class Booking(models.Model):

    """
    Бронирование
    """

    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    job = models.ForeignKey(
        Job,
        verbose_name='Рабочее место',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    datetime_from = models.DateTimeField(
        verbose_name='Дата начала',
        blank=False,
        null=False
    )

    datetime_to = models.DateTimeField(
        verbose_name='Дата окончания',
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'бронирование'
        verbose_name_plural = 'Бронирования'

    # def __str__(self):
    #     return f'Бронирование {self.job.name}'