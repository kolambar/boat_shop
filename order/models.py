from django.db import models

# Create your models here.


class Order(models.Model):

    boat = models.ForeignKey('boat.Boat', on_delete=models.CASCADE, verbose_name='Лодка')
    name = models.CharField(max_length=150, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта', unique=True)
    message = models.TextField(verbose_name='Сообщение')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время отправления заявки')
    closed = models.BooleanField(default=False, verbose_name='Заказ закрыт')

    def __str__(self):
        return f'{self.boat} от {self.email}'

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'