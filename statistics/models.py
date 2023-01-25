from django.db import models


class Statistics(models.Model):
    date = models.DateField(auto_now=True, verbose_name='Время создания')
    views = models.IntegerField(verbose_name='Количество просмотров')
    clicks = models.IntegerField(verbose_name='Количество кликов')
    cost = models.DecimalField(max_digits=999, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'Номер счетчика {self.pk}'
