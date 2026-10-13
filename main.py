from consoleUI import consoleUI
from person import Person
from calculator import BirthdayCalculator
from reprository import SaveData
from datetime import datetime

def main():
    ui = consoleUI()
    calculator = BirthdayCalculator()
    while True:
        choice = ui.show_menu()
        choice = int(choice)
        if choice == 1:
            data = ui.initialize_data()
            person = Person(data['name'], data['year'], data['month'], data['day'])
            result = calculator.calculate(person.name, person.year, person.month, person.day)
            ui.show_result(result=result)
            name, age_turning, next_birthday_in_days = result
            repo = SaveData()
            dob = datetime(data['year'], data['month'], data['day']).date()
            repo.save_to_csv(name,dob , age_turning, next_birthday_in_days)
        elif choice == 2:
            repo = SaveData()
            repo.load_data()
        elif choice == 3:
            break
        else:
            print("Oops! enter a number from 1 - 3!")
            continue

if __name__ =="__main__":
    main()
