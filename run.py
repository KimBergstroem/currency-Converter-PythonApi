'''
Travel Guide - Currency Converter
-------------------------------------------------------------
Made by: Kim Bergstroem
'''

import sys, time, os, requests, gspread
import time
from google.oauth2.service_account import Credentials
from modules.converter import display_meny_exchange
from modules.ascii_art import display_welcome_title, display_welcome_meny # Adds ascii art text headings
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

def welcome_message(): # Welcome Message
    """
    Displaying Welcome Message along with ASCII HEADING
    """
    display_welcome_title()
    time.sleep(1)
    message = (f"{t.bold}Hello and welcome! I hope you will find this guide useful! \n")
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    user_name = input(f"{t.bold}Please let me know your name and press ENTER: ").capitalize()
    print(f"{t.green}{t.bold}Thank you! and welcome once again {user_name} to this Traveling Guide!{t.end}")
    time.sleep(3)
    os.system('clear')


def welcome_meny(): # Welcome Meny
    """
    Welcome message for the user
    User is asked to input their name
    """
    while True:
        display_welcome_meny()
        user_nav = int(input(f"Enter you number here: "))
        if user_nav == 1:
            display_meny_country()
            break
        elif user_nav == 2:
            display_meny_currency_code()
            break
        elif user_nav == 3:
            os.system('clear')
            display_meny_exchange()
            os.system('clear')
        elif user_nav == 4:
            print(f"I Hope you enjoyed the Travel Guide! I will se you next time!!" )
            break
        else:
            print("You choice wrong number, pick again")

def display_meny_country(): # Country Display
    """
    Will display all countries in the world and display the currency in that specific country
    Will ask user, were to travel
    """
    print("Were do you want to travel?")
    welcome_meny()

def display_meny_currency_code(): # Country Currency Code
    """
    Will display the correct currency code, if user doesnt know the correct 3 letter code
    """
    print("Here you have a list of all country currency codes that you can use for exchange")
    welcome_meny()



def main(): # Main Start Function
    """
    Will run all everything
    """
    welcome_message()
    welcome_meny()

main()
