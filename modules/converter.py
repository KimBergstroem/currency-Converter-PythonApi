'''
Currency Converter 
-------------------------------------------------------------
API from Fixer API - https://apilayer.com/
'''
import requests
from modules.text_colors import TextColors # Adds color to text
t = TextColors # Declaring the function to smaller variabel

def convert_currency():
    while True:
        init_currency = input('Enter currency code, you would like to convert from: ')
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
   convert_currency()