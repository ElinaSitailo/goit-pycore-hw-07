from models.Record import Record
from models.AddressBook import AddressBook
import Command


class CommandManager:

    contacts = AddressBook()

    @staticmethod
    def clear_contacts():
        CommandManager.contacts.clear()

    @staticmethod
    def add_contact_command(args):
        if len(args) < 2:
            return f"Error: {Command.ADD_CONTACT.value}  command requires a name and a phone number."

        name = args[0]
        phone = args[1]

        record = CommandManager.contacts.get(name)
      

        try:
            is_not_found = record is None
            if is_not_found:
                record = Record(name)

            record.add_phone(phone)
            CommandManager.contacts.set_record(record)
            return f"Contact '{name}' with phone '{phone}' {"added" if is_not_found else "updated"} successfully."
        
        except ValueError as e:
            return f"Error: {e}"

    @staticmethod
    def update_contact_command(args):
        if len(args) < 3:
            return f"Error: '{Command.UPDATE_CONTACT.value}' command requires a name and an old phone number and a new phone number ."

        name = args[0]
        old_phone = args[1]
        new_phone = args[2]

        record = CommandManager.contacts.get(name)
        if not record:
            return f"Error: Contact '{name}' does not exist."

        try:
            record.edit_phone(old_phone, new_phone)
            return f"Contact '{name}' updated with new phone '{new_phone}'."
        except ValueError as e:
            return f"Error: {e}"

    @staticmethod
    def show_contact_command(args):
        if len(args) < 1:
            return f"Error: {Command.SHOW_CONTACT.value} command requires a name."

        name = args[0]
        record = CommandManager.contacts.get(name)
        if not record:
            return f"Error: Contact '{name}' does not exist."

        return str(record)

    @staticmethod
    def show_all_contacts_command():
        if len(CommandManager.contacts) == 0:
            return "No contacts found to show."

        output_lines = []
        for record in CommandManager.contacts.values():
            output_lines.append(str(record))
        return "\n".join(output_lines)

    @staticmethod
    def add_contact_birthday_command(args):
        if len(args) < 2:
            return f"Error: '{Command.ADD_BIRTHDAY.value}' command requires a name and a birthday (YYYY-MM-DD)."

        name = args[0]
        birthday_str = args[1]

        record = CommandManager.contacts.get(name)
        if not record:
            return f"Error: Contact '{name}' does not exist."

        try:
            record.set_birthday(birthday_str)
            return f"Birthday '{birthday_str}' added to contact '{name}'."
        except ValueError as e:
            return f"Error: {e}"

    @staticmethod
    def show_contact_birthday_command(args):
        if len(args) < 1:
            return f"Error: '{Command.SHOW_BIRTHDAY.value}' command requires a name."

        name = args[0]
        record = CommandManager.contacts.get(name)
        if not record:
            return f"Error: Contact '{name}' does not exist."

        birthday = record.birthday.value
        if not birthday:
            return f"Contact '{name}' does not have a birthday set."

        return f"Contact '{name}': Birthday: {birthday}"

    @staticmethod
    def show_upcoming_birthdays_command():
        upcoming_birthdays = CommandManager.contacts.get_upcoming_birthdays()
        if not upcoming_birthdays:
            return "No  birthdays found in upcoming 7 days."

        output_lines = []
        output_lines.append("Upcoming birthdays:")
        for record in upcoming_birthdays.values():
            output_lines.append(f"{record.name}: Birthday: {record.birthday.value}")
        return "\n".join(output_lines)
