from lesson import Multiplication, Division
import os
import time
import json
from datetime import date
from crawler import DirectoryCrawler

dc = DirectoryCrawler()

def set_up():
        count = 0
        streaks = dc.collector('streak.json')
        if not streaks:
            print("Add some new users -->")
            create_users()
            set_up()
        else:
            records = get_streaks(streaks[0])
            user = input("Hello there!!! Who are you???\t").casefold()
            if user not in records:
                print("Sorry, I do not remember you.")
                time.sleep(3)
                os.system("cls")
            else:
                print(f'Welcome back {user}\n'
                      f'You have been active for {records[user]['days_active']} days')
                time.sleep(3)
                run = True
                while run:
                    run = start_practice(user, count)
                    count += 1


def create_users():
    no_of_users = get_choice(1, 100, "How many users do you want to create?\t")
    users = []
    records = {}
    for i in range(no_of_users ):
        name = input(f'Enter a name for user {i + 1}\t').casefold()
        users.append(name)
    for user in users:
        records.update({user: {"days_active": 0, "last_date": date.today().isoformat(), "today": date.today().isoformat()}})
    records.update({"test": {"days_active": 0, "last_date": date.today().isoformat(), "today": date.today().isoformat()}})
    with open('streak.json', 'w+') as log:
        json.dump(records, log, indent = 4)


def get_streaks(streaks):
    with open((str)(streaks), 'r') as log:
        records = json.load(log)
        return records
    

def get_choice(low, high, message):
    choice = -1
    while not(choice >= low and choice <=high):
        try:
            choice = (int)(input(message))
            os.system("cls")
        except ValueError as _:
            os.system("cls")
            print(f'Enter a number from {low} to {high}')
    return choice


def start_practice(user, count):
    os.system("cls")
    print(f'You have completed {count} lessons today.')
    match(get_choice(0, 2, "Enter 1 for multiplication\n"
        "Enter 2 for Division\n"
        "Enter 0 to quit...\n"
        "Choice -->\t")):
            case 1:
                print("Multiplication Practice!!!")
                multiplication = Multiplication(get_choice(2, 100, "Enter a number to practice:\t"))
                if multiplication.solve_problem():
                    update_streaks(user)
                count += 1
                time.sleep(2)
                return True
                
            case 2:
                print("Division Practice!!!")
                division = Division(get_choice(2, 100, "Enter a number to practice:\t"))
                if division.solve_problem():
                    update_streaks(user)
                count += 1
                return True
                
            case 0:
                print(f"Bye {user}. See you later.....\n"
                      f"You completed {count} lessons.")
                time.sleep(3)
                os.system("cls")
                return False
        

def get_user():
    return input("Hello!!! Who is this???\t")


def update_streaks(user):
    records = get_streaks('streak.json')

    if records[user]['last_date'] < date.today().isoformat() and \
        records[user]['last_date'] != records[user]['today']:
        records[user]['days_active'] += 1
        records[user]['last_date'] = date.today().isoformat()
        records[user]['today'] = date.today().isoformat()
    
    with open('streak.json', 'w+') as log:
        json.dump(records, log, indent=4)

    print(f'{user} has a {records[user]['days_active']}-day streak')
    time.sleep(3)


if __name__ == "__main__":
    print("Let's practice maths!!!")
    set_up()   
