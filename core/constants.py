from drf_spectacular.utils import extend_schema


DAYS_OF_WEEK = [
    (1, 'Понедельник'),
    (2, 'Вторник'),
    (3, 'Среда'),
    (4, 'Четверг'),
    (5, 'Пятница'),
    (6, 'Суббота'),
    (7, 'Воскресенье'),
]

SCORES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

USERS_API_SCHEMA_EXTENSIONS = {
    'list': extend_schema(summary="Получить список пользователей"),
    'update': extend_schema(summary="Изменения данных о пользователе"),
    'partial_update': extend_schema(
        summary="Частичное изменение данных о пользователе",
        description="Изменения данных о пользователе. Поля, "
                    "которые не заполнены будут оставлены без изменений."
    ),
    'create': extend_schema(summary="Создать нового пользователя"),
    'destroy': extend_schema(summary="Удалить пользователя"),
    'retrieve': extend_schema(summary="Получить данные о пользователе")
}

CARWASH_API_SCHEMA_EXTENSIONS = {
    'list': extend_schema(summary="Получить список автомоек"),
    'retrieve': extend_schema(summary="Получить данные для карточки мойки")
}
