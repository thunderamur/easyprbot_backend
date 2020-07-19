from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class EventType(models.Model):
    name = models.CharField('тип события', max_length=255)

    class Meta:
        verbose_name = 'тип события'
        verbose_name_plural = 'типы событий'

    def __str__(self):
        return self.name


class Event(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.PROTECT)
    type = models.ForeignKey(EventType, verbose_name='тип события', on_delete=models.PROTECT)
    title = models.CharField('заголовок', max_length=255)
    description = models.TextField('описание', default='', blank=True)
    start_time = models.DateTimeField('дата/время')
    notified = models.BooleanField(verbose_name='уведомлен', default=False, blank=True)

    class Meta:
        verbose_name = 'событие'
        verbose_name_plural = 'события'
        ordering = ['start_time']

    def __str__(self):
        return f'{self.type}: {self.title} - {self.start_time}'
