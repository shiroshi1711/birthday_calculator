#5 sesi /20 menit, + 5 menit
#debug
from datetime import datetime as dt, timedelta as td
import json
import csv

class DataCLass:
    def __init__(self, name, dob, age):
        self.name = name
        self.dob = dob
        self.age = age

    def to_dict(self):
        datas = {
            "name" : self.name,
            "dob" : self.dob.strftime("%Y-%m-%d"),
            "age" : self.age
        }
        return datas
    
class BirthdayManager:
    def __init__(self, filename):
        self.filename = filename
        self.datalist = []

    def load_data(self):
        self.datalist.clear()
        try:
            with open (self.filename,  "r") as file:
                datas = json.load(file)
                for data in datas:
                    data =DataCLass(data['name'], dt.strptime(data['dob'],"%Y-%m-%d").date(), data['age'])
                    self.datalist.append(data)
        except ValueError:
            print("Error loading file!")

    def save_data(self):
        if not self.datalist:
            return
        dictdata = []
        for data in self.datalist:
            data = data.to_dict()
            dictdata.append(data)
        try:
            with open (self.filename, "w") as file:
                json.dump(dictdata, file, indent= 4)
        except ValueError:
            print("Error saving to JSON!")

    def add_data(self):
        while True:
            try:
                name = input("Enter the name: ").strip().capitalize()
                for data in self.datalist:
                    if name == data.name:
                        print("Name already exist! pick a more unique name")
                        continue
                year = self.get_valid_year()
                month = self.get_valid_month()
                day = self.get_valid_day()
                age = self.count_age()
                new_data = DataCLass(name,dt(year,month,day).date(),age)
                self.datalist.append(new_data)
            except ValueError:
                print("failed to add data!")
                continue
    
    def remove_data(self):
        if not self.datalist:
            print("No data to remove!")
            return                  #belum kelar

    def clear_all(self):
        if not self.datalist:
            print("No datas to be cleared!")
            return
        else:
            self.datalist.clear()
            print("All datas are cleared!")
            return

    def sort_data(self):
        if not self.datalist:
            print("List is empty! no data to sort")
            return
        print("Sort by: ")
        print("1. sort by age")
        print("2. sort by name")
        print("3. back to main menu")
        print()
        while True:
            try:
                c = int(input("Enter a number: "))
                if c == 1:
                    self.sort_by_age()
                elif c == 2:
                    self.sort_by_name()
                elif c == 3:
                    break
                else:
                    print("Oops! choose a number from 1 - 3")
                    continue
            except ValueError:
                print("Invalid input! enter a number like 1 , 2..")
                continue

    def import_to_csv(self):
        if not self.datalist:
            print("List is empty! add some data to import first!")
            return
        filename = "birthdaydata.csv"
        try:
            with open (filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    'name',
                    'date of birth',
                    'age'
                ])
                for data in self.datalist:
                    writer.writerow([
                        data.name,
                        data.dob,
                        data.age
                    ])
                print("Saved to CSV!")
        except  Exception as e:
            print(f"Error saving to CSV : {e}")

    def show_data(self):
        if not self.datalist:
            print("List is empty, no data to display!")
            return
        print(f'{"Data":^40}')
        print("="*40)
        print("{:<15} {:<15} {:10}".format("Name","Date of birth", "Age"))
        for i, data in enumerate(self.datalist, 1):
            print(f"{i}. {data.name.capitalize():<13}{data.dob.strftime('%Y-%m-%d'):<15}{data.age:<10}")


    def sort_by_age(self):
        sorteddata = sorted(self.datalist, key= lambda data : data.age)
        print(f'{"Sorted by age":^40}')
        print("="*40)
        print("{:<15} {:<15} {:10}".format("Name","Date of birth", "Age"))
        for i, data in enumerate(sorteddata, 1):
            print(f"{i}. {data.name.capitalize():<13}{data.dob.strftime('%Y-%m-%d'):<15}{data.age:<10}")


    def sort_by_name(self):
        sorteddata = sorted(self.datalist, key= lambda data : data.name)
        print(f"{'Sorted by name':^40}")
        print("="*40)
        print("{:<15} {:<15} {:10}".format("Name","Date of birth", "Age"))
        for i, data in enumerate(sorteddata, 1):
            print(f"{i}. {data.name.capitalize():<13}{data.dob.strftime('%Y-%m-%d'):<15}{data.age:<10}")


    def get_valid_year(self):
        while True:
            try:
                year = int(input("Enter birth year: "))
                today_year = dt.now().year
                if year < 1500 or year > today_year:
                    print("Invalid input! try again")
                    continue     #benahin ntr
                return year
            except ValueError:
                print("Invalid input! enter a number like 1990 or 2010!")
                continue

    def get_valid_month(self):
        while True:
            try:
                month = int(input("Enter birth month: "))
                if month <=0 or month > 12:
                    print("Invalid input! month must be 1-12!")
                    continue
                return month
            except ValueError:
                print("Invalid input! enter the number of the month (e.g., 1 for January, 3 for March etc)")
                continue

    def leap_year_check(self, year):
        leap = False
        year = self.get_valid_year()
        if (year % 4 == 0 ) and (year % 100 != 0 or year % 400 == 0):
            leap = True
        return leap

    def get_valid_day(self, month):
        leap = self.leap_year_check()
        days_limit = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if leap:
            days_limit[2] = 29
        while True:
            try:
                day = int(input("Enter birth date: "))
                if day <= 0 or day > days_limit[month]:
                    print("Invalid input! day must be within limit day of the month! ")
                    continue
                return day
            except ValueError:
                print("Invalid input! enter a number like 1, 10, 15")
                continue

    def count_age(self):
        today_year = dt.now().year
        year = self.get_valid_year()
        age = today_year - year
        return age



filename = "birthdaydata.json"
manager = BirthdayManager(filename)

manager.load_data()

while True:
    print(f"\n=== Birthday Manager ===")
    print("1. Add data")
    print("2. Remove data")
    print("3. Sort data")
    print("4. Clear all data")
    print("5. Import to CSV")
    print("6. Show all data")
    print("7. Exit")
    print()
    try:
        c = int(input("Choose a number from 1 to 7: "))
        print()
        if c == 1:
            manager.add_data()
        elif c == 2:
            manager.remove_data()
        elif c == 3:
            manager.sort_data()
        elif c == 4:
            manager.clear_all()
        elif c == 5:
            manager.import_to_csv()
        elif c == 6:
            manager.show_data()
        elif c == 7:
            manager.save_data()
            print("Goodbye! your data is saved!")
            break
        else:
            print("Oops! please choose a number from 1 t0 7!")
    except ValueError:
        print("Invalid input! enter a number like 1, 4")
