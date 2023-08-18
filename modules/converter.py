"""
Currency Converter
-------------------------------------------------------------
API from Fixer API - https://apilayer.com/
"""
import requests
import os
import dotenv
from modules.currency_data import currency_dict
from modules.ascii_art import display_menu_exchange_title
from modules.text_colors import TextColors  # Adds color to text

t = TextColors  # Declaring the function to smaller variabel


def display_menu_exchange():
    """
    Currency Converter function
    Compares two - 3 letters currency code with convertion
    """
    display_menu_exchange_title()

    while True:
        while True:
            init_currency = input(
                "Enter currency code you would like to convert from: "
            ).upper()
            if init_currency in currency_dict:
                break
            else:
                print(
                    f"{t.red}Sorry, the currency you entered is not in the"
                    f" list. Try again{t.end} "
                )

                while True:
                    show_data = input(
                        "Do you wanna se the list with available currency"
                        f" codes? ({t.green}y{t.end} /"
                        f" {t.red}n{t.end}): \n"
                    ).upper()
                    if "N" not in show_data and "Y" not in show_data:
                        print(f"{t.red}Please press either Y or N{t.end}")
                    if "Y" in show_data:
                        for key, value in currency_dict.items():
                            print(
                                f"Code: {t.cyan}{key}{t.end} Country:"
                                f" {t.cyan}{value}{t.end}"
                            )
                            print("------------------")
                        break
                    elif "N" in show_data:
                        break
                    else:
                        continue
        while True:
            target_currency = input(
                "Enter currency code you would like to convert to: "
            ).upper()
            if target_currency in currency_dict:
                break
            else:
                print(
                    f"{t.red}Sorry, the currency you entered is not in the"
                    f" list. Try again{t.end}"
                )
        while True:
            try:
                amount = float(input("Enter the amount: "))
            except BaseException:
                print(f"{t.red}The amount must be a numeric value!{t.end}")
                continue
            if not amount > 0:
                print(f"{t.red}The amount must be greater than 0{t.end}")
                continue
            else:
                break
        url = (
            "https://api.apilayer.com/fixer/convert?to="
            + target_currency
            + "&from="
            + init_currency
            + "&amount="
            + str(amount)
        )

        dotenv.load_dotenv()
        api_key = os.getenv("API_KEY")
        payload = {}
        headers = {"apikey": api_key}
        response = requests.request(
            "GET", url, headers=headers, data=payload
        )
        status_code = response.status_code

        if status_code != 200:
            print(
                f"{t.red}Uh oh, there was a problem. Please Restart the"
                f" application and try again later{t.end}"
            )
        else:
            result = response.json()
            print("Conversion result: " + str(result["result"]))
        while True:
            repeat = input(
                f"Do you wanna convert again? ({t.green}Y{t.end} /"
                f" {t.red}N{t.end}): \n"
            ).upper()
            if "N" not in repeat and "Y" not in repeat:
                print(
                    f'{t.red}Please press either "Y" for YES or "N" for'
                    f' NO{t.end}'
                )
            if repeat == "N":
                print(
                    f"You are redirected back to main menu, wait a second"
                )
                return repeat
            elif repeat == "Y":
                os.system("clear")
                display_menu_exchange_title()
                break
            else:
                continue


if __name__ == "__main__":
    display_menu_exchange()
