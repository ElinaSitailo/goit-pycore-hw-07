from .Field import Field


class Name(Field):
    def __init__(self, value):
        if not value.isalpha():
            raise ValueError("Name must contain only alphabetic characters.")
        super().__init__(value)
