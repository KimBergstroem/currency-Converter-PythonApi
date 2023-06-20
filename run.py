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
    while True:
        user_name = input(f"{t.bold}Please let me know your name and press {t.bold}{t.underline}ENTER{t.end}: ").capitalize()
        if validate_name(user_name):
            print(f"{t.green}{t.bold}Thank you! and welcome once again {user_name} to this Traveling Guide!{t.end}")
            time.sleep(3)
            os.system('clear')
            break
        else:
            continue
    return user_name

def welcome_meny(user_name): 
    """
    Welcome message for the user
    User is asked to input their name
    """
    while True:
        display_welcome_meny()
        while True:
            user_input_int = validate_number(f"Please {t.green}{t.bold}{user_name}{t.end}, Enter your number here and press {t.bold}{t.underline}ENTER{t.end}: ")            
            if user_input_int == 1:
                display_meny_country(user_name)
                break
            elif user_input_int == 2:
                display_meny_currency_code()
                break
            elif user_input_int == 3:
                os.system('clear')
                display_meny_exchange()
                os.system('clear')
            elif user_input_int == 4:
                print(f"I Hope you enjoyed the Travel Guide! I will se you next time!!" )
                break
            else:
                if user_input_int > 4 or user_input_int < 1:
                    print(f"{t.red}Only number 1 to 4 can be chosen!{t.end}" )
                    continue

def display_meny_country(user_name): # Alternative 1 in meny - Country Display
    """
    Will display all countries in the world and display the currency in that specific country
    Will ask user, were to travel
    """
    #PRINT OUT THE CONTENTS
    content_worksheet = SHEET.worksheet("content")
    content_values = content_worksheet.row_values(1) #Which display the different content in the first row
    content_input = input(f"What content do you want to travel to?")
    content_message = (f"This Content can be chosen to visist:\n{t.cyan}{t.bold}" + " - ".join(content_values))
    print(content_message)
    welcome_meny(user_name)

def display_meny_currency_code(): # Alternative 2 in meny - Country Currency Code
    """
    Will display the correct currency code, if user doesnt know the correct 3 letter code
    """
    print("Here you have a list of all country currency codes that you can use for exchange")
    welcome_meny()


def validate_name(name):
    """
    Check for a name with 3 or more letters
    Check for only letters
    """
    try:
        if len(name) < 3:
            raise ValueError(
                f"{t.red}Name should contain least 3 letters and you gave us {len(name)}!{t.end}"
            )
        for letter in name:
            if not letter.isalpha():
                raise ValueError(
                    f"{t.red}We can only accept letters from A to Z.{t.end}"
                )
    except ValueError as e:
        print(f"{t.red}Obs!{t.end} {e} {t.red}Try again!{t.end}\n")
        return False
    return True

def validate_number(number):
    """
    Validate that user enters correct integer instead of string
    """
    while True:
        try:
            userInput = int(input(number))       
        except ValueError:
            print(f"{t.red}Try again.{t.end} Please choose from 1-4 as the meny shows above!!")
            continue
        else:
            return userInput 
            break 
         

def main(): # Main Start Function
    """
    Will run all everything
    """
    user_name = welcome_message()
    welcome_meny(user_name)

main()
