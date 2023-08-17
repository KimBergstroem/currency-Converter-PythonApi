'''
Travel Guide - Currency Converter
-------------------------------------------------------------
Made by: Kim Bergstroem
'''
import sys
import time
import os
import requests
import gspread
import dotenv
from gspread.exceptions import APIError
from google.oauth2.service_account import Credentials
from modules.currency_data import currency_dict
from modules.converter import display_menu_exchange
from modules.ascii_art import display_welcome_title, display_welcome_menu, display_menu_country_title, display_menu_currency_code_title
from modules.text_colors import TextColors  # Adds color to text

t = TextColors  # Declaring the function to smaller variabel

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
    message = (f"{t.bold}Hello and welcome! I hope you will find this guide useful!\n")
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


def welcome_menu(user_name):
    """
    Welcome message for the user
    User is asked to input their name
    """
    while True:
        display_welcome_menu()
        user_input_int = validate_number(f"Please {t.green}{t.bold}{user_name}{t.end}, Enter your number here and press {t.bold}{t.underline}ENTER{t.end}: ")
        if user_input_int == 1:
            os.system('clear')
            display_menu_country(user_name)
            break
        elif user_input_int == 2:
            os.system('clear')
            display_menu_currency_code(user_name)
            break
        elif user_input_int == 3:
            os.system('clear')
            if not display_menu_exchange():
                return  # Return to the main menu
            os.system('clear')
        elif user_input_int == 4:
            print(" ")
            print(f"Thank you {t.green}{t.bold}{user_name}{t.end} for this time!")
            print(f"I Hope you enjoyed this {t.green}{t.bold}Travel Guide{t.end}! I will see you next time!!{t.end}")
            time.sleep(3)
            os.system('clear')
            quit()
        else:
            if user_input_int > 4 or user_input_int < 1:
                print(f"{t.red}Only number 1 to 4 can be chosen!{t.end}")
                continue


def display_menu_country(user_name):  # Alternative 1 in menu - Country Display
    """
    Will display all countries in the world and specific currency
    Will ask user, were to travel
    """
    LINE_UP = '\033[1A'     # Module Time function, Move up n(=1) lines
    LINE_CLEAR = '\x1b[2K'  # Module Time function, Erase current line


    # PRINT OUT THE CONTENTS
    display_menu_country_title()
    print(f"{t.bold}Let us help you decide where to travel with a brief questionnaire!...{t.end} ")
    print(LINE_UP, end=LINE_CLEAR)
    # Block user input while printing
    press_enter_to_continue("\nPress Enter to continue...")

    while True:
        try:
            content_worksheet = SHEET.worksheet("content")      # Declaring variabel from the worksheet that can be used in the code below
            content_keys = content_worksheet.row_values(1)      # Which display the different content in the first row
            content_message = (f"This Continent can be chosen to visit: " + f"\n " + f"\n{t.cyan}{t.bold}" + " - ".join(content_keys))
            print(content_message)
            print(" ")
            user_content = validation_user_input(f"{t.end}What continent in the world are you interested in?\nChoose a content and press {t.bold}{t.underline}ENTER:{t.end} ", content_message)
            key_value = user_content

            print(f"This countries can be choosen in the content {t.cyan}{t.bold}{user_content}{t.end}")
            print(" ")
            if user_content in key_value:
                first_row_values = content_worksheet.row_values(1)              # 1. Creating another variabel for displaying all the worksheets first row values "africa","america","asia","europa"
                column_index = first_row_values.index(key_value) + 1            # 2. Creating another variabel for checking our first row values for the key heading variabel we are searching for. We use + 1 becouse the first column are [0]
                column_values = content_worksheet.col_values(column_index)      # 3. We create another variabel that will be assigned the first column and all that values that are in the same column, in this case "Africa".
                for value in column_values:                                     # 4. Using a loop, we iterate through each value in column_values, printing each value to the terminal.
                    print(f"{t.cyan}{t.bold}{value}{t.end}")
            print(" ")
            user_country = validation_user_input(f"What country in the wonderful continent of {t.cyan}{t.bold}{user_content}{t.end} would you like to visit?\nChoose a country and press {t.bold}{t.underline}ENTER:{t.end} ", column_values)
            user_saved_data = press_enter_to_continue(f"You have been choosing {t.cyan}{t.bold}{user_content}{t.end} and country {t.cyan}{t.bold}{user_country}{t.end}. Great choice!\nPress {t.bold}{t.underline}ENTER{t.end} to see what currency that are used in that country!")
            print("Please wait for the currency to load...")
            currency_worksheet = SHEET.worksheet("currency")  # Declaring variabel from the worksheet that can be used in the code below
            key_value = currency_worksheet.col_values(1, 1)   # Get the value of the first cell in the first row which contain "country".
            num_rows = len(currency_worksheet.col_values(1))  # Get the total number of rows in the worksheet.

            found = False  # Flag to check if the user_country is found in the worksheet.

            # Iterate over the rows starting from the second row (index 1).
            for i in range(1, num_rows):
                country = currency_worksheet.cell(i, 1).value  # Get the value of the cell in the current row and the country column.

                if country == user_country:
                    found = True
                    row_values = currency_worksheet.row_values(i)
                    print(f"In the country {t.cyan}{t.bold}{user_country}{t.end} they are using the currency\n" + f"\n" + f"{t.cyan}{t.bold}" + " - ".join(row_values))
                    break
            if not found:
                print("Country not found.")
            print(" ")
            print(f"{t.end}If you do not have this currency,\nwe recommend you to go to our {t.cyan}{t.bold}Exchange service{t.end} in the main menu!")
            print(" ")
        except APIError as e:
            error_message = (f"{t.red}An error occurred while accessing the server: Too many requests per minute.\nPlease wait 25sec! Go back to the main menu and check out other stuff in the meantime!{t.end}")
            print(error_message)

        while True:
            repeat_input = input(f"Do you wanna try another travel destination? Type ({t.bold}{t.green}Y{t.end}) and press {t.bold}{t.underline}ENTER{t.end}\nGo back to main menu? Type {t.end}({t.bold}{t.red}N{t.end}) and press {t.bold}{t.underline}ENTER{t.end} \n").upper()
            if "N" not in repeat_input and "Y" not in repeat_input:
                print(f'{t.red}Please press either "Y" for YES or "N" for NO{t.end}')
            if "Y" in repeat_input:
                os.system('clear')
                display_menu_country_title()
                break
            elif "N" in repeat_input:
                os.system('clear')
                welcome_menu(user_name)
                break
            else:
                continue


def display_menu_currency_code(user_name):  # Alternative 2 in menu - Country Currency Code
    """
    Will display the correct currency code, if user doesnt know the correct 3 letter code
    """
    display_menu_currency_code_title()
    time.sleep(1)
    message = (f"Here you will find a list with all 3 Letters codes and country! \nBe sure to scroll {t.bold}up{t.end} and {t.bold}down{t.end} to get full overview over the list!\n")
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("Loading the list, please wait")
    time.sleep(2)
    print(" ")
    for i in range(101):
        print('\r', str(i), end='%')
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
    while True:
        repeat = input(f"Go back to main menu, Press {t.bold}{t.underline}ENTER{t.end}\n").upper()
        if repeat == "":
            os.system('clear')
            welcome_u(user_name)
            break
        else:
            continue


#  Validation functions START HERE
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


def press_enter_to_continue(user_saved_data):
    """
    Check for pressed key "ENTER" to continue with the application
    Checks for user press "ENTER" on the keyboard
    """
    while True:
        try:
            if user_saved_data == "":
                break
            else:
                print("Please press only the 'Enter' key to continue.")
        except KeyboardInterrupt:
            print("\nExiting...")
            exit()


def validate_number(number):
    """
    Validate that user enters correct integer instead of string
    """
    while True:
        try:
            userInput = int(input(number))
        except ValueError:
            print(f"{t.red}Try again.{t.end} Please choose from 1-4 as the menu shows above!!")
            continue
        else:
            return userInput
            break


def validation_user_input(question, valid_values):
    """
    Checks and compares the user input to the valid values
    """
    while True:
        user_input = input(question).capitalize().strip()  # Remove leading/trailing spaces
        if user_input == "":
            print(f"{t.red}Please enter a valid input.{t.end}")
        elif user_input not in valid_values:
            print(f"{t.red}Sorry, the content you entered is not in the list above. Try again.{t.end}")
        else:
            return user_input


def main():  # Main Start Function
    """
    Will run all everything
    """
    user_name = welcome_message()
    welcome_menu(user_name)


main()
