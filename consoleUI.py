from datetime import datetime

class consoleUI:
  
    def initialize_data(self):
        name = self.name_input()
        year = self.year_input()
        month = self.month_input()
        day = self.day_input(year=year, month=month)
        data = {
            "name": name,
            "year" :year,
            "month" : month,
            "day" : day
            }
        return data

    def show_result(self, result):
        name, age_turning, days_left = result
        today = datetime.today().date()
        print(f"Today is {today}")
        if days_left == 0:
            print(f"{name} is turning {age_turning} today!, Happy birthday!")
        else:
            print(f"{name} will be turning {age_turning} in {days_left} days!")

    def show_menu(self):
        print("{:^83}".format("BIRTHDAY CALCULATOR"))
        print("=" * 83)
        print("1. Input data")
        print("2. Load data")
        print("3. Exit")
        while True:
            choice = input("Enter a number: ")
            print()
            if choice.isdigit():
                return choice
            else:
                print("Enter a number from 1-3")
                continue
             
    def name_input(self):
        while True:
            try:
                name = input("Enter name: ").strip().capitalize()
                if not name:
                    print("Name cant be empty!")
                    continue
            except  Exception as e:
                print(f"Something went wrong! {e}")
            return name
        
    def year_input(self):
        today_year = datetime.now().year
        while True:
            try:
                year = input("Enter birth year(e.g., 2000, 1990): ")
                if year.isdigit():
                    year = int(year)
                    if year < 1800:
                        print("Invalid input!")
                        continue
                    if year > today_year:
                        print('Invalid input!')
                        continue
                else:
                    print("Enter a number!")
                    continue
            except Exception as e:
                print(f"Oops!, something went wrong {e}")
            return year

    def month_input(self):
        while True:
            try:
                month = input("Enter birth month(e.g., 1 - 12):" )
                if month.isdigit():
                    month = int(month)
                    if month < 1 or month > 12:
                        print("Invalid input!")
                        continue
                else:
                    print("Enter a number!")
                    continue
            except Exception as e:
                print(f"Oops! something went wrong {e}")
            return int(month)

    def day_input(self, year, month):
        max_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        is_leap = False
        if (year % 4 == 0) and (year % 100 != 0 or year % 400 ==0):
            is_leap = True
        if is_leap:
            max_days[2] = 29
        while True:
            try:
                day = input("Enter birth day(e.g., 1-31): ")
                if day.isdigit():
                    day = int(day)
                    if day < 1 or day > max_days[month]:
                        print("Invalid input!")
                        continue
                else:
                    print("Enter a number!")
                    continue
            except Exception as e:
                print(f"Something went wrong! {e}")
            return day
