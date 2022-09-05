import random
import os
import string


settings = {
    'lower case letters': 1,
    'upper case letters': 1,
    'numbers': 1,
    'symbols': 1,
    'length': 8
}


def clear_screen():
    os.system("cls")


def user_config_settings(settings):
    print('-'*5, 'Configuration Settings', '-'*5, '\n', sep='')
    for item in settings.keys():
        if item == 'length':
            while True:
                user_input = input(
                    "Count of characters (default : 8, enter/default) : ")
                if user_input == '':
                    user_input = str(settings[item])
                if user_input.isdigit():
                    user_input = int(user_input)
                    if 4 < user_input < 30:
                        settings[item] = user_input
                        break
                    else:
                        print("ERR The entered number is too small or big")
                else:
                    print("ERR You should enter numbers")
                print("Try again\n")
            continue
        while True:
            user_input = input(
                f"Include {item} (default : {settings[item]}, yes/y, no/n, enter/default) : ")
            if user_input in ['y', 'n', '']:
                if user_input == 'n':
                    settings[item] = 0
                elif user_input == 'y':
                    settings[item] = 1
                break
            else:
                print("ERR Invalid input")
                print("Try again\n")


def generate_password(settings):
    length = settings['length']
    configs = list(filter(lambda x: settings[x] == 1, list(settings.keys())))
    while True:
        password = ''
        for _ in range(length):
            choice = random.choice(configs)
            if choice == 'lower case letters':
                password += random.choice(string.ascii_lowercase)
            elif choice == 'upper case letters':
                password += random.choice(string.ascii_uppercase)
            elif choice == 'numbers':
                password += random.choice("0123456789")
            elif choice == 'symbols':
                password += random.choice(""" ~!@#$%^&*()_+=}{":;'/\\.,`[]""")

        print('-'*20, f"GENERATED PASSWORD : {password}", '-'*20, sep='\n')
        want_another_password = input(
            "Do yo want another password (yes/y, no/n, enter/yes) ?")
        if want_another_password in ['', 'y', 'n']:
            if want_another_password == 'n':
                print("Thanks for using us")
                break
           
        else:
            print("ERR Invalid input")
            print('Try again')


def run():
    clear_screen()
    user_config_settings(settings)
    generate_password(settings)


run()