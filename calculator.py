from datetime import datetime

class BirthdayCalculator:

    def calculate(self, name, year, month, day):
        birthday = datetime(year, month, day).date()
        today = datetime.now().date()
        if birthday.year == ((year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)) and birthday.month == 2 and birthday.day == 29:
            birthday = datetime(year, 3, 1).date()
        next_birthday = datetime(today.year, birthday.month, birthday.day).date()
        age_turning = today.year - birthday.year
        if next_birthday < today:
            next_birthday = datetime((today.year + 1), birthday.month, birthday.day).date()
            age_turning = (today.year + 1) - birthday.year
        days_left = (next_birthday - today).days
        if next_birthday == today:
            days_left = 0
        return (name, age_turning, days_left)