import sys

sys.path.append("./")  # Or the path to your module's parent directory

import inspect
import Command
from CommandManager import CommandManager


def check_contact_data_lenth_is_0_after_init():

    assert len(CommandManager.contacts.data) == 0


check_contact_data_lenth_is_0_after_init()

TEST_NAME = "Vasya Pupkin"
TEST_NAME2 = "Marina Grabina"
PHONE1 = "1115551234"
PHONE2 = "2225551234"
PHONE3 = "3335551234"


def check_phone_is_added():
    print("\n" + inspect.currentframe().f_code.co_name)
    CommandManager.clear_contacts()
    CommandManager.add_contact_command([TEST_NAME, PHONE1])
    assert len(CommandManager.contacts.data) == 1
    assert TEST_NAME in CommandManager.contacts.data
    assert PHONE1 == CommandManager.contacts.data[TEST_NAME].phones[0].value
    print(CommandManager.show_contact_command([TEST_NAME]))


check_phone_is_added()


def check_the_second_phone_is_added():
    print("\n" + inspect.currentframe().f_code.co_name)
    CommandManager.clear_contacts()
    print(CommandManager.add_contact_command([TEST_NAME, PHONE1]))
    print(CommandManager.add_contact_command([TEST_NAME, PHONE2]))
    assert len(CommandManager.contacts.data) == 1
    assert TEST_NAME in CommandManager.contacts.data
    assert PHONE2 == CommandManager.contacts.data[TEST_NAME].phones[1].value
    print(CommandManager.show_contact_command([TEST_NAME]))


check_the_second_phone_is_added()


def check_the_second_same_phone_is_not_added():
    print("\n" + inspect.currentframe().f_code.co_name)
    CommandManager.clear_contacts()
    print(CommandManager.add_contact_command([TEST_NAME, PHONE1]))
    print(CommandManager.add_contact_command([TEST_NAME, PHONE2]))
    print(CommandManager.show_all_contacts_command())


def check_the_second_phone_is_updated():
    print("\n" + inspect.currentframe().f_code.co_name)
    CommandManager.clear_contacts()
    print(CommandManager.add_contact_command([TEST_NAME, PHONE1]))
    print(CommandManager.add_contact_command([TEST_NAME, PHONE2]))
    print(CommandManager.update_contact_command([TEST_NAME, PHONE2, PHONE3]))
    assert len(CommandManager.contacts.data) == 1
    assert TEST_NAME in CommandManager.contacts.data
    assert PHONE3 == CommandManager.contacts.data[TEST_NAME].phones[1].value
    print(CommandManager.show_contact_command([TEST_NAME]))


check_the_second_phone_is_updated()


def check_show_all():
    print("\n" + inspect.currentframe().f_code.co_name)
    CommandManager.clear_contacts()
    CommandManager.add_contact_command([TEST_NAME, PHONE1])
    CommandManager.add_contact_command([TEST_NAME, PHONE2])
    CommandManager.add_contact_command([TEST_NAME2, PHONE3])
    assert len(CommandManager.contacts.data) == 2
    print(CommandManager.show_all_contacts_command())


check_show_all()


def check_is_birthday_added():
    print("\n" + inspect.currentframe().f_code.co_name)
    CommandManager.clear_contacts()
    print(CommandManager.add_contact_command([TEST_NAME, PHONE1]))
    print(CommandManager.add_contact_birthday_command([TEST_NAME, "11.12.1980"]))
    print(CommandManager.show_contact_birthday_command([TEST_NAME]))


check_is_birthday_added()


def check_show_upcoming_birthdays_command():
    print("\n" + inspect.currentframe().f_code.co_name)
    CommandManager.clear_contacts()
    print(CommandManager.add_contact_command([TEST_NAME, PHONE1]))
    print(CommandManager.add_contact_birthday_command([TEST_NAME, "01.11.1980"]))

    print(CommandManager.add_contact_command([TEST_NAME2, PHONE2]))
    print(CommandManager.add_contact_birthday_command([TEST_NAME2, "30.11.1980"]))

    print(CommandManager.show_upcoming_birthdays_command())


check_show_upcoming_birthdays_command()
