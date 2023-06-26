import sys, time, os, requests, gspread
import time
from google.oauth2.service_account import Credentials
from modules.currency_data import currency_dict
from modules.converter import display_meny_exchange
from modules.ascii_art import display_welcome_title, display_welcome_meny, display_meny_country_title,display_meny_currency_code_title # Adds ascii art text headings
from modules.text_colors import TextColors # Adds color to text
t = TextColors # Declaring the function to smaller variabel

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("travel_Guide")




def display_meny_currency_code(): # Alternative 2 in meny - Country Currency Code
    """
    Will display the correct currency code, if user doesnt know the correct 3 letter code
    """
    display_meny_currency_code_title()
    time.sleep(1)
    message = (f"Here you will find a list with all 3 Letters codes and country! \nBe sure to scroll {t.bold}up{t.end} and {t.bold}down{t.end} to get full overview over the list!\n")
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("Reloading the list, please wait")
    time.sleep(2)
    print(" ")
    for i in range(101):
        print('\r', str(i), end = '%')
        time.sleep(0.08)
        if i == 100:
            print(f" {t.white}{t.bold} - Complete{t.end}")
    print(" ")
    print(f"{t.bold}Checkout the list below:{t.end}")
    time.sleep(2.5)
    print(" ")
    for key, value in currency_dict.items():
        print(f"Code: {t.cyan}{t.bold}{key}{t.end} Country: {t.cyan}{t.bold}{value}{t.end}")
        print("------------------")


def main(): # Main Start Function
    """
    Will run all everything
    """
    display_meny_currency_code()
main()