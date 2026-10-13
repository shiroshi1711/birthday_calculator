import csv
from datetime import datetime

class SaveData:

    def save_to_csv(self, name, dob, age_turning, next_birthday_in_days):
        with open("data.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'dob', 'age_turning', 'next_birthday_in_days'])
            if file.tell() == 0:
                writer.writeheader()

            writer.writerow({
                "name" : name,
                "dob" : dob,
                "age_turning" : age_turning,
                "next_birthday_in_days" : next_birthday_in_days
            })

    def load_data(self):
        with open ("data.csv", "r", newline="", encoding="utf-8") as file:
            rows =  csv.DictReader(file)
            print("{:<83}".format("BIRTHDAY DATA"))
            print("today: ", datetime.today().date())
            print("=" * 83)
            print("{:<3}{:<20}{:<20}{:<20}{:<20}".format("No","Name", "DOB", "Age Turning", "Next B'day In Days"))
            for i, row in enumerate(rows, 1):
                print(f"{i:<3}{row['name']:<20}{row['dob']:<20}{row['age_turning']:<20}{row['next_birthday_in_days']:<20}")