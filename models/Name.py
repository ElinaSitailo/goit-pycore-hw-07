from .Field import Field
import re

class Name(Field):
    def __init__(self, value):
        
        if re.fullmatch(r"^[a-zA-Z ]*$", value) is None:
            raise ValueError("Name must contain only alphabetic and space characters.")
        super().__init__(value)
