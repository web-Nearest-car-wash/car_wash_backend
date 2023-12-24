# Generated by Django 4.2.8 on 2023-12-18 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0005_carwashimagemodel_carwashservicesmodel_and_more'),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота'), (7, 'Воскресенье')], verbose_name='День недели')),
                ('opening_time', models.TimeField(blank=True, null=True, verbose_name='Время открытия')),
                ('closing_time', models.TimeField(blank=True, null=True, verbose_name='Время закрытия')),
                ('around_the_clock', models.BooleanField(default=False, verbose_name='Круглосуточно')),
                ('carwash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='carwash.carwashmodel', verbose_name='Мойка')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
                'ordering': ('carwash',),
            },
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
