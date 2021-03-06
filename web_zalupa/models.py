from django.db import models


class ServiceDonate(models.Model):
    SELECT_TYPE = [
        ('prefix', 'Префикс'),
        ('rank', 'Привилегия'),
        ('other', 'Другое'),
    ]
    name = models.CharField('Название', max_length=255, default='Строитель')
    type = models.CharField('Тип', choices=SELECT_TYPE, default='prefix', max_length=16)
    command = models.TextField('Команда', default="/say Hello %_player%_!")
    price = models.IntegerField('Цена в рублях', max_length=255, default=100)

    def __str__(self):
        return "#%d Тип: %s - Название: \"%s\" (%d RUB)" % (self.id, self.type, self.name, self.price)

    class Meta:
        verbose_name = 'Донат-услуга'
        verbose_name_plural = 'Донат-услуги'


class ServiceDonateStatus(models.Model):
    STATUS_ = [
        ('wait', 'Ожидает'),
        ('paid', 'Оплачено'),
        ('done', 'Завершено'),
    ]
    name_player = models.CharField('Игрок', max_length=255, default='lomaka')
    status_pay = models.CharField('Статус', choices=STATUS_, default='wait', max_length=16)
    service_id = models.IntegerField('ID услуги')
    price = models.IntegerField('Сумма в рублях', default=0)
    user_id_bot = models.BigIntegerField('ID пользователя в боте', default=0)
    time = models.DateTimeField("Время", auto_now=True)
    bill_id_qiwi = models.CharField("Номер платежа QIWI (Bill ID)", unique=True, max_length=255, default=None)

    def __str__(self):
        return "#%d Игрок: %s - ID услуги: %s (%d RUB) Статус - %s | %s" % (
            self.id, self.name_player, self.service_id, self.price, self.status_pay, self.time
        )

    class Meta:
        verbose_name = 'Статус оплаты'
        verbose_name_plural = 'Статусы оплаты'


class SystemSettings(models.Model):
    name = models.CharField('Название', max_length=255, default=None)
    param = models.TextField('Значение', default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'


class BanInBot(models.Model):
    user_id = models.CharField('ID пользователя', unique=True, max_length=255, default=None)
    comment = models.TextField(
        'Комментарий (Его получит пользователь при попытке воспользоваться ботом)',
        default="Команда Zalupa решила что тебя нужно заблокировать."
    )

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = 'Бан'
        verbose_name_plural = 'Бан-лист'
