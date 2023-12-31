# Generated by Django 4.2.8 on 2023-12-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_alter_schedulemodel_day_of_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulemodel',
            name='closing_time',
            field=models.TimeField(blank=True, help_text='Введите время в формате ЧЧ:ММ, например 10:00', null=True, verbose_name='Время закрытия'),
        ),
        migrations.AlterField(
            model_name='schedulemodel',
            name='opening_time',
            field=models.TimeField(blank=True, help_text='Введите время в формате ЧЧ:ММ, например 10:00', null=True, verbose_name='Время открытия'),
        ),
    ]
