# Generated by Django 4.2.8 on 2023-12-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0016_alter_carwashimagemodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carwashmodel',
            name='metro',
        ),
        migrations.AlterField(
            model_name='carwashimagemodel',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Фото автомойки'),
        ),
        migrations.RemoveField(
            model_name='carwashmodel',
            name='type',
        ),
        migrations.DeleteModel(
            name='NearestMetroStationModel',
        ),
        migrations.AddField(
            model_name='carwashmodel',
            name='type',
            field=models.ManyToManyField(null=True, to='carwash.carwashtypemodel', verbose_name='Тип автомойки'),
        ),
    ]
