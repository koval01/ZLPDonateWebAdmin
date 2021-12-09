from django.db import models


class ServiceDonate(models.Model):
    SELECT_TYPE = [
        ('prefix', 'Префикс'),
        ('rank', 'Привилегия'),
    ]
    name = models.CharField('Название', max_length=255, default='Випка')
    type = models.CharField('Тип', choices=SELECT_TYPE, default='prefix', max_length=16)
    command = models.TextField('Команда', default="/say Hello &player&!")
    price = models.IntegerField('Цена в рублях', max_length=255, default=100)

    def __str__(self):
        return "Тип: %s - Игрок: %s (%d RUB)" % (self.type, self.name, self.price)

    class Meta:
        verbose_name = 'Донат-услуга'
        verbose_name_plural = 'Донат-услуги'


class ServiceDonateStatus(models.Model):
    STATUS_ = [
        ('wait', 'Ожидает'),
        ('done', 'Оплачено'),
    ]
    name_player = models.CharField('Игрок', max_length=255, default='lomaka')
    status_pay = models.CharField('Статус', choices=STATUS_, default='wait', max_length=16)
    service_id = models.IntegerField('ID услуги')
    price = models.IntegerField('Сумма в рублях', default=0)

    def __str__(self):
        return "#%d Игрок: %s - ID услуги: %s (%d RUB) Статус - %s" % (
            self.id, self.name_player, self.service_id, self.price, self.status_pay
        )

    class Meta:
        verbose_name = 'Статус оплаты'
        verbose_name_plural = 'Статусы оплаты'
