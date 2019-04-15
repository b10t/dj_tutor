from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошёл активацияю ?')
    send_messages = models.BooleanField(default=True, verbose_name='Слать оповещения о новых комментариях ?')

    class Meta:
        pass
        # db_table = ''
        # managed = True
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

