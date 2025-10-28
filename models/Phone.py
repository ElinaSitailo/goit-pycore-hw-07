from .Field import Field
import re

MIN_PHONE_LEN = 10
MAX_PHONE_LEN = 12
EMPTY_PHONE = ""


class Phone(Field):
    def __init__(self, inphone):
        phone = re.sub(r"\D", "", inphone)  # Remove all non-digit characters

        if phone == EMPTY_PHONE:
            raise ValueError("Phone number cannot be empty.")

        if not phone.isdigit() or len(phone) < MIN_PHONE_LEN:
            raise ValueError(f"Phone number must be at least {MIN_PHONE_LEN} digits.")
        
        if len(phone) > MAX_PHONE_LEN:
            phone = phone[:MAX_PHONE_LEN]  # Truncate to max length

        super().__init__(phone)

