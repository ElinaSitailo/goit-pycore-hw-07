from .Field import Field

MIN_PHONE_LEN = 10


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) < MIN_PHONE_LEN:
            raise ValueError(
                f"Phone number must be at least {MIN_PHONE_LEN} digits and contain only numbers."
            )
        super().__init__(value)
