# Generated by Django 4.2.8 on 2023-12-14 20:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarWashTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Тип автомойки')),
            ],
            options={
                'verbose_name': 'Тип автомойки',
                'verbose_name_plural': 'Типы автомоек',
            },
        ),
        migrations.CreateModel(
            name='CarWashModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Название')),
                ('coordinates', models.CharField(blank=True, max_length=200, validators=[django.core.validators.RegexValidator(message='Неверные координаты', regex='^-?([0-8]?[0-9]|90)(\\.[0-9]{1,10}),([0-9]{1,2}|1[0-7][0-9]|180)(\\.[0-9]{1,10})$')], verbose_name='Координаты Ш,Д')),
                ('loyalty', models.TextField(default=None, max_length=500, null=True, verbose_name='Лояльность')),
                ('price_list', models.CharField(default=None, max_length=500, null=True, verbose_name='Прайс лист')),
                ('legal_person', models.BooleanField(default=False, verbose_name='Работа с юр лицами')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carwash.carwashtypemodel', verbose_name='Тип автомойки')),
            ],
            options={
                'verbose_name': 'Автомойка',
                'verbose_name_plural': 'Автомойки',
            },
        ),
    ]
