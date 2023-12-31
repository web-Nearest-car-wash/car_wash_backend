from datetime import datetime
from decimal import Decimal

from django.conf import settings
from django.db.models import Q
from django_filters.rest_framework import (BooleanFilter, CharFilter,
                                           FilterSet, NumberFilter)

from carwash.models import CarWashModel
from schedule.models import ScheduleModel


class CarWashFilter(FilterSet):
    """Фильтрация моек по местоположению, типу,
    услугам, режиму работы и рейтингу"""

    high_rating = BooleanFilter(
        method='filter_high_rating',
        label='Оценка 4+')

    is_around_the_clock = BooleanFilter(
        method='filter_is_around_the_clock',
        label='Круглосуточный режим работы'
    )

    is_open = BooleanFilter(
        method='filter_is_open',
        label='Автомойка открыта на данный момент'
        )

    latitude = NumberFilter(
        method='filter_by_distance',
        label='Координаты пользователя: широта'
        )

    longitude = NumberFilter(
        method='filter_by_distance',
        label='Координаты пользователя: долгота')

    services = CharFilter(
        method='filter_services',
        label='Услуги: название услуг через запятую без пробелов'
    )

    type = CharFilter(
        field_name='type__name',
        lookup_expr='istartswith',
        label='Тип автомойки'
    )

    class Meta:
        model = CarWashModel
        fields = ['latitude', 'longitude', 'services']

    def filter_by_distance(self, queryset, name, value):
        """Фильтрация по местоположени """
        latitude = self.data.get('latitude')
        longitude = self.data.get('longitude')
        if latitude and longitude:
            return queryset.filter(
                Q(latitude__range=(
                    Decimal(latitude) - Decimal(settings.LAT_RANGE),
                  Decimal(latitude) + Decimal(settings.LAT_RANGE))) &
                Q(longitude__range=(
                    Decimal(longitude) - Decimal(settings.LONG_RANGE),
                  Decimal(longitude) + Decimal(settings.LONG_RANGE)))
            )
        return queryset

    def filter_services(self, queryset, name, value):
        """Фильтрация по услугам"""
        if value:
            services_list = value.split(',')
            for service in services_list:
                queryset = queryset.filter(
                    service__name__icontains=service.strip()
                )
            return queryset
        return queryset

    def filter_is_open(self, queryset, name, value):
        """Фильтрация по статусу - открыто/закрыто"""
        now = datetime.now().time()
        day_of_week = datetime.now().weekday()
        open_carwashes = ScheduleModel.objects.filter(
            Q(day_of_week=day_of_week,
              opening_time__lte=now,
              closing_time__gte=now) | Q(
                day_of_week=day_of_week,
                around_the_clock=True
            )
        ).values_list('carwash')
        if value:
            return queryset.filter(id__in=open_carwashes)
        return queryset

    def filter_is_around_the_clock(self, queryset, name, value):
        """Фильтрация по круглосуточному режиму работы"""
        day_of_week = datetime.now().weekday()
        around_the_clock_carwashes = ScheduleModel.objects.filter(
            day_of_week=day_of_week,
            around_the_clock=True
        ).values_list('carwash')
        if value:
            return queryset.filter(id__in=around_the_clock_carwashes)
        return queryset

    def filter_high_rating(self, queryset, name, value):
        """Фильтрация моек с высоким рейтингом"""
        if value:
            queryset = queryset.filter(rating__gte=4)
            return queryset
        return queryset
