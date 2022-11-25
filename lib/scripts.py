import os
from time import sleep
from lib.api_request import get_quote, get_address


def main_options():
    os.system('cls')
    print(open('lib\\title.txt', 'r').read())
    print(f'\n\n{"Choose an option":^50}\n\n1- Currency quote\n2- Address by zip code\n3- Exit')
    c = 0
    while True:
        op = input('> ')
        if op == '1': currency_quote(); break
        elif op == '2': address_detail(); break
        elif op == '3': close_app()
        else:
            if c == 3: main_options(); break
            print('\nChoose a valid option.'); c+=1


def currency_quote():
    print(f'\n{"downloading data...":^50}')
    usd, eur, btc = get_quote('usd'), get_quote('eur'), get_quote('btc')
    os.system('cls')
    print(f'\n\tDOLLAR\t\tR$ {usd}\n\tEURO\t\tR$ {eur}\n\tBITCOIN\t\tR$ {btc}')


def address_detail():
    cep = input('\nCEP: ')
    print(f'\n{"please wait...":^50}')
    shot = get_address(cep)
    if shot[0]:
        os.system('cls')
        print(shot[1])
    else:
        print(shot[1])


def end_options():
    sleep(1.5)
    print('\n\n1- Home\n2- Exit')
    c = 0
    while True:
        choice = input('> ')
        if choice == '1': break
        elif choice == '2': close_app()
        else:
            if c == 3:
                print(f'\n{"redirecting to Home...":^50}')
                sleep(1.1)
                break
            print('\nChoose a valid option.')
            c+=1


def close_app():
    print(f'\n{"closing app...":^50}')
    sleep(1.3)
    exit()
