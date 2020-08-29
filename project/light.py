import time
from colorama import Fore, Back, Style
from os import system


def red(t):
    # print(Back.GREEN + 'and with a green background')
    # print(Style.DIM + 'and in dim text')

    while t != 6:
        print(Fore.RED + '■')
        print('', t)
        time.sleep(1)
        t = t + 1
        system('cls')

    print(Style.RESET_ALL)


def green(t):
    while t != 5:
        print(Fore.GREEN + '  ■')
        print('  ',t)
        time.sleep(1)
        t = t + 1
        system('cls')

    print(Style.RESET_ALL)


def yellow(t):
    while t != 2:
        print(Fore.YELLOW + '    ■')
        print('    ', t)
        time.sleep(1)
        t = t + 1
        system('cls')


    print(Style.RESET_ALL)


while True:
    t = 1
    red(t)
    system('cls')
    green(t)
    system('cls')
    yellow(t)
    system('cls')