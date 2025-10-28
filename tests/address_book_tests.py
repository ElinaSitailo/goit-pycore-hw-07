"""
Tests for the AddressBook class.
This module contains tests for address book management functionality.
"""

import sys

sys.path.append("./")  # Or the path to your module's parent directory

from datetime import date, timedelta

from models.AddressBook import AddressBook
from models.Record import Record


def check_contact_data_lenth_is_0_after_init():
    book = AddressBook()
    assert len(book.data) == 0


check_contact_data_lenth_is_0_after_init()


def check_contact_data_lenth_is_1_after_record_adding():
    book = AddressBook()
    record = Record("John Doe")
    record.add_phone("1234567890")
    book.add_record(record)
    assert len(book.data) == 1
    assert "John Doe" in book.data


check_contact_data_lenth_is_1_after_record_adding()


def check_contact_is_found_by_name():
    book = AddressBook()
    record = Record("John Doe")
    book.add_record(record)

    found = book.find("John Doe")
    assert found is not None
    assert found.name.value == "John Doe"


check_contact_is_found_by_name()


def check_upcoming_birthdays():
    book = AddressBook()

    record1 = Record("Alice")
    record1.set_birthday("15.10.1990")
    book.add_record(record1)

    record2 = Record("Bob")
    record2.set_birthday("20.10.1985")
    book.add_record(record2)

    record3 = Record("Charlie")
    record3.set_birthday("25.12.1992")
    book.add_record(record3)

    # Set a fixed current date for testing
    test_now_date = date(2023, 10, 14)
    upcoming = book.get_upcoming_birthdays(days_ahead=7, now_date=test_now_date)

    assert len(upcoming) == 2
    assert any(rec.name.value == "Alice" for rec in upcoming.values())
    assert any(rec.name.value == "Bob" for rec in upcoming.values())


check_upcoming_birthdays()
