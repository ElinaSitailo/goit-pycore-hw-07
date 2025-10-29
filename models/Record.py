from .Name import Name
from .Phone import Phone
from .Birthday import Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def set_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def edit_phone(self, old_phone_number, new_phone_number):

        old_phone =  Phone(old_phone_number)
        new_phone =  Phone(new_phone_number)

        for i, phone in enumerate(self.phones):
            if phone.value == old_phone.value:
                self.phones[i] = new_phone
                return
        raise ValueError("Phone number to update is not found.")

    def __str__(self):
        return f"Contact name: {self.name.value}{"" if self.birthday == None else f", birthday {self.birthday.value}"}, phones: {'; '.join(p.value for p in self.phones)}"
