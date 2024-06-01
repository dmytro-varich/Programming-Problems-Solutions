from datetime import datetime

import constants


class Movie:
    def __init__(self, title, length, genre, age_limit, release_date):

        # title
        if not isinstance(title, str):
            raise TypeError("Movie title must be string")

        # length
        if not isinstance(length, int):
            raise TypeError("Movie length must be integer")
        elif length <= 0:
            raise ValueError("Movie length must be at least 1")

        # genre
        if genre not in constants.GENRES:
            raise ValueError(f'Unknown genre "{genre}"')

        # age_limit
        if not isinstance(age_limit, int):
            raise TypeError("Age limit must be integer")
        elif age_limit <= 0:
            raise ValueError("Age limit must be at least 1")

        self.title = title
        self.length = length
        self.genre = genre
        self.age_limit = age_limit
        self.validate_date(release_date)  # validate_date(self, date)
        self.release_date = release_date

    def validate_date(self, date):

        if not isinstance(date, str):
            raise TypeError("Release date must be string")

        if date.count('/') != 2 or date[4] != '/' or date[7] != '/':
            raise ValueError("Release date must meet format YYYY/MM/DD")

        year, month, day = date.split('/')
        try:
            year1 = int(year)
            month1 = int(month)
            day1 = int(day)
        except ValueError:
            raise ValueError(f'Could not load date from string: "{date}"')

        if month1 == 0:
            raise ValueError(f"Invalid month 0")
        elif month1 > 12 or month1 < 1:
            raise ValueError(f"Invalid month {month}")

        try:
            datetime.strptime(date, '%Y/%m/%d')
        except ValueError:
            if day == '00':
                raise ValueError(f"Invalid day for {constants.MONTHS.get(month)}: 0")
            else:
                raise ValueError(f"Invalid day for {constants.MONTHS.get(month)}: {day}")

    def get_time_passed(self, date):

        self.validate_date(date)

        if date == self.release_date:
            return 0

        date1 = datetime.strptime(date, '%Y/%m/%d').date()
        date2 = datetime.strptime(self.release_date, '%Y/%m/%d').date()

        delta = date1 - date2

        # print(delta, " = ", date1, ' - ', date2)
        return delta.days


if __name__ == '__main__':
    # you can run your tests here
    pass


