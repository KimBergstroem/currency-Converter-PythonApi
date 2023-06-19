'''
Currency Converter 
-------------------------------------------------------------
API from Fixer API - https://apilayer.com/
'''
import requests, os
from run.py import inputNumber
from modules.currency_data import currency_dict
from modules.ascii_art import display_meny_exchange_title
from modules.text_colors import TextColors # Adds color to text
t = TextColors # Declaring the function to smaller variabel

def display_meny_exchange():
    """
    Currency Converter function
    Compares two - 3 letters currency code with convertion
    """
    display_meny_exchange_title()

    while True:
        while True:
            init_currency = input('Enter currency code you would like to convert from: ').upper()
            if init_currency in currency_dict:
                break
            else:
                print("Sorry, the currency you entered is not in the list. Try again ")

                while True:
                    show_data = input(f"Do you wanna se the list with available currency codes? ({t.green}y{t.end} / {t.red}n{t.end}): \n").upper()
                    if "N" not in show_data and "Y" not in show_data:
                        print(f"Please press either {t.green}y{t.end} or {t.red}n{t.end}")
                    if "Y" in show_data:
                        for key, value in currency_dict.items():
                            print(f"Code: {t.cyan}{key}{t.end} Country: {t.cyan}{value}{t.end}")
                            print("------------------")
                        break
                    elif "N" in show_data:
                        break
                    else:
                        continue

        while True:
            target_currency = input('Enter currency code you would like to convert to: ').upper()
            if target_currency in currency_dict:
                break
            else:
                print("Sorry, the currency you entered is not in the list. Try again")
                
        while True:
            try:
                amount = float(input('Enter the amount: '))
            except:
                print('The amount must be a numeric value!')
                continue

            if not amount > 0:
                print('The amount must be greater than 0')
                continue
            else:
                break

        url = ('https://api.apilayer.com/fixer/convert?to='
                + target_currency + '&from=' + init_currency +
                '&amount=' + str(amount))

        payload = {}
        headers = {'apikey': 'Wyf6JKlmEnpBYW6kzAUSsoo0ptkUz5lr'}
        response = requests.request('GET', url, headers=headers, data=payload)
        status_code = response.status_code

        if status_code != 200:
            print('Uh oh, there was a problem. Please Restart the application and try again later')
            quit()

        result = response.json()
        print('Conversion result: ' + str(result['result']))

        repeat = input(f"Do you wanna convert again? ({t.green}y{t.end} / {t.red}n{t.end}): \n").upper()
        if repeat != "Y" :
            break
        else:
            os.system('clear')
            display_meny_exchange_title()
            continue



if __name__ == '__main__':
   display_meny_exchange()