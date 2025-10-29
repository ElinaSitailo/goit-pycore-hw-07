from Command import Command
from CommandManager import CommandManager
from models.Birthday import Birthday
from models.Phone import Phone


def parse_input(user_input):
    if len(user_input.strip()) == 0:
        return ("",)
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def get_output_by_command(command, args):
    is_exit = False

    if command == Command.ADD_CONTACT:
        output = CommandManager.add_contact_command(args)
    elif command == Command.UPDATE_CONTACT:
        output = CommandManager.update_contact_command(args)
    elif command == Command.SHOW_CONTACT:
        output = CommandManager.show_contact_command(args)
    elif command == Command.SHOW_ALL_CONTACTS:
        output = CommandManager.show_all_contacts_command()

    elif command == Command.ADD_BIRTHDAY:
        output = CommandManager.add_contact_birthday_command(args)
    elif command == Command.SHOW_BIRTHDAY:
        output = CommandManager.show_contact_birthday_command(args)
    elif command == Command.SHOW_UPCOMING_BIRTHDAYS:
        output = CommandManager.show_upcoming_birthdays_command()
    elif command == Command.HELLO:
        output = "How can I help you?"
    elif command == Command.HELP or command == Command.HELP_ALT:
        output = (
            "Available commands:\n"
            f"{Command.HELLO} - Greet the bot\n"
            f"{Command.ADD_CONTACT} <name> <phone> - Add a new contact. Expected phone lenght is at least {Phone.MIN_PHONE_LEN} digits.\n"
            f"{Command.UPDATE_CONTACT} <name> <old_phone> <new_phone> - Change an existing contact's phone number. Expected phone lenght is at least {Phone.MIN_PHONE_LEN} digits.\n"
            f"{Command.SHOW_CONTACT} <name> - Show the phone number of a contact\n"
            f"{Command.SHOW_ALL_CONTACTS} - Show all contacts\n"
            f"{Command.ADD_BIRTHDAY} <name> <{Birthday.BIRTHDAY_FORMAT}> - Add birthday to a contact\n"
            f"{Command.SHOW_BIRTHDAY} <name> - Show birthday of a contact\n"
            f"{Command.SHOW_UPCOMING_BIRTHDAYS} - Show contacts with upcoming birthdays\n"
            f"{ Command.EXIT_1}, { Command.EXIT_1}, { Command.EXIT_3} - Exit the program"
        )
    elif command in (Command.EXIT_1, Command.EXIT_2, Command.EXIT_3):
        output = "Goodbye!"
        is_exit = True
    else:
        output = "Unknown command. Please try again."

    return output, is_exit


if __name__ == "__main__":

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        output, is_exit = get_output_by_command(command, args)
        print(output)
        if is_exit:
            break
