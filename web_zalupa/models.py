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
        return "%s - %s (%d RUB)" % (self.type, self.name, self.price)

    class Meta:
        verbose_name = 'Донат-услуга'
        verbose_name_plural = 'Донат-услуги'


class ServiceDonateStatus(models.Model):
    STATUS_ = [
        ('wait', 'Ожидает'),
        ('done', 'Оплачено'),
    ]
    nameService = models.CharField('Услуга', max_length=255, default='Випка')
    namePlayer = models.CharField('Игрок', max_length=255, default='lomaka')
    statusPay = models.CharField('Статус', choices=STATUS_, default='wait', max_length=16)
    price = models.IntegerField('Цена в рублях', max_length=255)

    def __str__(self):
        return "%s - %s (%d RUB) Статус - %s" % (
            self.namePlayer, self.nameService, self.price, self.statusPay
        )

    class Meta:
        verbose_name = 'Статус оплаты'
        verbose_name_plural = 'Статусы оплаты'