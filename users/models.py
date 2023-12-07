from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USERS_ROLES = (
        (USER, 'Пользователь'),
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
    )
    role = models.CharField(
        'Пользовательская роль',
        max_length=max(len(role) for role, none_ in USERS_ROLES),
        choices=USERS_ROLES,
        default=USER,
    )
    phone = PhoneNumberField(
        'Номер телефона',
        max_length=20,
        blank=True,
        null=True,
        unique=True,
        # validators=RegexValidator(
        #     r'^\+?\d{11}$',
        #     message='Номер телефона должен быть в формате +79999999999'
        # )
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


from django.db import models


class Car(models.Model):
    class CarType(models.TextChoices):
        CAR = 'car', 'Легковой автомобиль'
        CVC = 'cvc', 'Внедорожник'
        TRUCK = 'truck', 'Грузовой автомобиль'

    brand = models.CharField(
        'Марка автомобиля',
        max_length=50
    )
    model = models.CharField(
        'Модель автомобиля',
        max_length=50
    )
    type = models.CharField(
        'Тип автомобиля',
        max_length=max(len(type) for type, none_ in CarType.choices),
        choices=CarType.choices
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='cars',
        verbose_name='Пользователь',
        null=True,
        blank=True,
    )
