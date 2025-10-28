from .Field import Field
from datetime import datetime

class Birthday(Field):
    def __init__(self, value: str):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
            birthday_date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(birthday_date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

