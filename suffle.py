import random
import datetime

def is_weekday():
    today = datetime.datetime.today().weekday()
    return today < 5

def make_menu(week_end : list, week_day : list) -> dict:
    menu = {
        'Lunch' : '',
        'Dinner' : ''
    }
    if is_weekday():
        menu['Lunch'] = random.choice(week_day)
        menu['Dinner'] = random.choice(week_day)
    else:
        menu['Lunch'] = random.choice(week_end)
        menu['Dinner'] = random.choice(week_end)

    return menu

if __name__ == '__main__':
    make_menu()
    