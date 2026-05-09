#start 09-05-2026 05.39 PM
from datetime import datetime as dt, timedelta as td
import csv
import json

class BirthdayData:
    def __init__(self, name, year, month, day):
        self.name = name.capitalize()
        self.year = int(year)
        self.month = int(month)                             #kayanya ini atributnya mending langsung dob jangan di pisah gini
        self.day = int(day)                                 #atau kalo emng mau dipisah bikin atribut sendiri buat dob nya biar
                                                            #biar kalo mau manggil gak ribet
    def to_dict(self):
        dictdata ={
            "name" : self.name,
            "year" : str(self.year),
            "month" : str(self.month),
            "day" : str(self.day)
        }
        return dictdata
    
class BirthdayManager:
    def __init__(self, filename):
        self.filename = filename
        self.birthday_list = []

    def load_data(self):
        self.birthday_list.clear()
        while True:
            try:
                with open (self.filename, "r") as file:
                    data = json.load(file)
                    for d in data:
                        d = BirthdayData(d['name'],d['year'],d['month'], d['day'])
                        self.birthday_list.append(d)
            except FileNotFoundError:
                print("No saved birthday data! starting with empty list!")
                break
        
    def save_to_json(self):
        dictlist= []
        if not self.birthday_list:
            print("no data to save! input some first!")
            return
        for data in self.birthday_list:
            data = data.to_dict()
            dictlist.append(data)
        while True:
            try:
                with open (self.filename, 'w') as file:
                    json.dump(dictlist, file, indent= 4)
                    print("Saved to JSON!")
            except ValueError:
                print('Error saving to JSON!')

    def get_valid_day(self):
        pass

    def get_valid_month(self):
        pass

    def get_valid_year(self):
        pass

    def leap_year_check(self):
        leap = False
        year = self.get_valid_year()
        if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
            leap = True
        return leap

    def next_birthday(self):
        pass

    def sort_birthday(self):
        pass

    def delete_birthday(self):
        pass

    def days_left(self):
        pass

    def export_data_to_csv(self):
        filename = 'birthdaymanager.csv'
        try:
            with open(filename, 'w', newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "name",
                    'date of birth'
                    'age'
                    'next birthday in'
                ])
                for data in self.birthday_list:                 #biar bisa di tulis di sini kayanya harus di bikin variable sendiri dob nya
                    pass                                        #belum kelar nih
        except ValueError:
            print("error exporting to csv!")

filename = "birthdaymanager.json"
manager = BirthdayManager(filename)
manager.load_data()
while True:
    try:
        pass
    except ValueError:
        print(" ")


#oke tinggal bikin data managernya kek
#simpen data ultah masing2
#sortir biar tau ultahnya yg bentar lagi siapa
#itung berapa hari lagi ke next ulang tahun nya
#export data ke csv