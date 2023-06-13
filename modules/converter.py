'''
Currency Converter 
-------------------------------------------------------------
API from Fixer API - https://apilayer.com/
'''
import requests
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
            url = "https://api.apilayer.com/currency_data/list"
            payload = {}
            headers= {
                "apikey": "Wyf6JKlmEnpBYW6kzAUSsoo0ptkUz5lr"
            }
            response = requests.request("GET", url, headers=headers, data = payload)
            status_code = response.status_code
            result_list = response.text
            if status_code == 200:
                result_list = response.json()
                init_currency = input('Enter currency code, you would like to convert from: ')
                if init_currency in result_list.values():
                    break
                else:
                    print("Sorry, the currency you entered is not in the list. Try again")
            else:
                print("Failed to retrieve the currency list.")

        target_currency = input('Enter currency code, you would like to convert to: ')

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
            print('Uh oh, there was a problem. Please try again later')
            quit()

        result = response.json()
        print('Conversion result: ' + str(result['result']))

        repeat = input(f"Do you wanna convert again? ({t.green}y{t.end} / {t.red}n{t.end}): \n")
        if repeat != "y":
            break


if __name__ == '__main__':
   display_meny_exchange()