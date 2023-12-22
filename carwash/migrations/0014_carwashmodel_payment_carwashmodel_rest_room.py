# Generated by Django 4.2.8 on 2023-12-21 18:49

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0013_delete_promotionsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='carwashmodel',
            name='payment',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('cash', 'Наличные'), ('card', 'Картой'), ('online', 'Онлайн'), ('SBP', 'СБП')], help_text='Выберите способ оплаты', max_length=30, null=True, verbose_name='Способ оплаты'),
        ),
        migrations.AddField(
            model_name='carwashmodel',
            name='rest_room',
            field=models.BooleanField(default=False, help_text='Наличие комнаты отдыха', verbose_name='Комната отдыха'),
        ),
    ]
