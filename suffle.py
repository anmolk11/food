import random
import datetime

def is_weekday():
    today = datetime.datetime.today().weekday()
    # Monday = 0, Tuesday = 1, ..., Friday = 4
    # Return True if it's a weekday (Monday to Friday)
    return today < 5

def make_menu(week_end : list, week_day : list) -> dict:
    menu = {
        'Lunch' : [],
        'Dinner' : []
    }
    if is_weekday():
        menu['Lunch'].append(random.choice(week_day))
        menu['Dinner'].append(random.choice(week_day))
    else:
        menu['Lunch'].append(random.choice(week_end))
        menu['Dinner'].append(random.choice(week_end))
        
    return menu

if __name__ == '__main__':
    make_menu()
    