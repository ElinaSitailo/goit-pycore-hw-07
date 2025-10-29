from collections import UserDict
from datetime import date, datetime, timedelta


class AddressBook(UserDict):
    DAYS_AHEAD = 7

    def set_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Record not found.")

    def find(self, name):
        return self.data.get(name, None)

    def get_upcoming_birthdays(
        self, days_ahead: int = 7, now_date: date = datetime.now().date()
    ):

        if now_date is None:
            now_date = datetime.now()

        #print(f"\nNOW DATE IS: {now_date}, days ahead: {days_ahead}")

        upcoming_birthdays = {}

        for record in self.data.values():
            if record.birthday is not None:
                birth_date = record.birthday
                # print(
                #     f"\nProcess birth date for name: {record.name}, birth date: {birth_date}"
                # )

                try:

                    this_year_birthday = birth_date.value.replace(year=now_date.year)
                    #print(f"This year's birthday: {this_year_birthday}")

                    # If birthday has already occurred this year, consider next year's birthday
                    if this_year_birthday < now_date:
                        this_year_birthday = this_year_birthday.replace(
                            year=now_date.year + 1
                        )
                        print(f"Next year's birthday: {this_year_birthday}")

                    else:
                        this_year_birthday_weekday = this_year_birthday.weekday()

                        # Adjust for weekends (Saturday and Sunday)
                        if this_year_birthday_weekday == 6:  # Sunday
                            this_year_birthday += timedelta(days=1)  # Move to Monday
                            #print(f"Adjusted birthday, Sunday: {this_year_birthday}")
                        elif this_year_birthday_weekday == 5:  # Saturday
                            this_year_birthday += timedelta(days=2)  # Move to Monday
                            #print(f"Adjusted birthday, Saturday: {this_year_birthday}")

                        days_until_birthday = (this_year_birthday - now_date).days
                        # print(
                        #     f"Days until birthday: {days_until_birthday}, weekday: {this_year_birthday_weekday}"
                        # )

                        if 0 <= days_until_birthday <= days_ahead:
                            upcoming_birthdays[record.name.value] = record
                            # print(
                            #     f"Added to upcoming birthdays: {record.name}, {birth_date}"
                            # )

                except Exception as e:
                    print(f"Error processing birthday for {record.name}: {e}")
                    continue

        return upcoming_birthdays
