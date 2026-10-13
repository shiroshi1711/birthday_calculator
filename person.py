from datetime import datetime

class Person:
    def __init__(self, name, year, month, day):
        if not name:
            raise Exception ("Name cant be empty!")
        today = datetime.today()
        dob = datetime(year=year, month=month, day=day)
        if dob > today:
            raise Exception ("Birth date cant be from future!")
        self.name = name
        self.year = year
        self.month = month
        self.day = day
        self.dob = dob
