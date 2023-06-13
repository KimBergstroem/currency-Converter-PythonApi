'''
Travel Guide - Currency Converter
-------------------------------------------------------------
Made by: Kim Bergstroem
'''

import sys, time, os, requests, gspread
import time
from google.oauth2.service_account import Credentials
from modules.converter import convert_currency
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

def welcome_message():
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
    user_name = input(f"{t.bold}Please let me know your name: ")
    print(f"{t.green}{t.bold}Thank you! and welcome once again {user_name} to this Traveling Guide!{t.end}")
    time.sleep(3)
    os.system('clear')


def welcome_meny():
    
    display_welcome_meny()
    while True:
        user_nav = int(input(f"Enter you number here: "))
        if user_nav == 1:
            display_meny_country()
            break
        elif user_nav == 2:
            display_meny_currency_code()
            break
        elif user_nav == 3:
            convert_currency()
            break
        else:
            print("You choice wrong number, pick again")

def display_meny_country():
    print("Were do you want to travel?")

def display_meny_currency_code():
    print("What do you want to convert")



def main():
    """
    Will run all everything
    """
    welcome_message()
    welcome_meny()

main()
