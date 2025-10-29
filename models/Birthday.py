from .Field import Field
from datetime import datetime


class Birthday(Field):
    BIRTHDAY_FORMAT = "DD.MM.YYYY"

    def __init__(self, value: str):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
            birthday_date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(birthday_date)
        except ValueError:
            raise ValueError(f"Invalid date format. Use {Birthday.BIRTHDAY_FORMAT}")

