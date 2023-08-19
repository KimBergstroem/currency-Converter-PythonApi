"""
Travel Guide - Currency Converter
-------------------------------------------------------------
Made by: Kim Bergstroem
"""
import sys
import time
import os
import requests
import gspread
import dotenv
import math
from gspread.exceptions import APIError
from google.oauth2.service_account import Credentials
from modules.currency_data import currency_dict
from modules.converter import display_menu_exchange
from modules.ascii_art import (
    display_welcome_title,
    display_welcome_menu,
    display_menu_country_title,
    display_menu_currency_code_title,
)
from modules.text_colors import TextColors  # Adds color to text

t = TextColors  # Declaring the function to smaller variabel

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
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

    print(
        f"{t.yellow}{t.bold}Hello and welcome! I hope you will find this"
        f" guide useful!\n{t.end}"
    )
    while True:
        user_name = input(
            f"{t.bold}Please let me know your name and press"
            f" {t.bold}{t.underline}ENTER{t.end}: "
        ).capitalize()
        if validate_name(user_name):
            print(
                f"{t.green}{t.bold}Thank you! and welcome once again"
                f" {user_name} to this Traveling Guide!{t.end}"
            )
            time.sleep(3)
            os.system("clear")
            break
        else:
            continue
    return user_name


def welcome_menu(user_name):
    """
    Welcome message for the user
    User is asked to input their name
    """
    # Declare menu options range
    min_option = 1
    max_option = 4

    while True:
        display_welcome_menu()
        user_input_int = validate_number(
            f"Please {t.green}{t.bold}{user_name}{t.end}, Enter your"
            f" number here and press {t.bold}{t.underline}ENTER{t.end}: ",
            min_option,
            max_option,
        )
        if user_input_int == 1:
            os.system("clear")
            display_menu_country(user_name)
            break
        elif user_input_int == 2:
            os.system("clear")
            display_menu_currency_code(user_name)
            break
        elif user_input_int == 3:
            os.system("clear")
            if not display_menu_exchange():
                return  # Return to the main menu
            os.system("clear")
        elif user_input_int == 4:
            print(" ")
            print(
                f"Thank you {t.green}{t.bold}{user_name}{t.end} for this"
                " time!"
            )
            print(
                f"I Hope you enjoyed this {t.green}{t.bold}Travel"
                f" Guide{t.end}! I will see you next time!!{t.end}"
            )
            time.sleep(3)
            os.system("clear")
            quit()


def display_menu_country(
    user_name,
):  # Alternative 1 in menu - Country Display
    """
    Will display all countries in the world and specific currency
    Will ask user, were to travel
    """
    LINE_UP = "\033[1A"  # Module Time function, Move up n(=1) lines
    LINE_CLEAR = "\x1b[2K"  # Module Time function, Erase current line

    # PRINT OUT THE CONTENTS
    display_menu_country_title()
    print(
        f"{t.bold}Let us help you decide where to travel with a brief"
        f" questionnaire!...{t.end}\n "
    )
    press_enter_to_continue(
        f"Type {t.bold}{t.underline}ENTER{t.end} to continue: "
    )

    print(LINE_UP, end=LINE_CLEAR)
    while True:
        try:
            # Declaring variabel from the worksheet that can be used in the
            # code below
            content_worksheet = SHEET.worksheet("content")
            # Which display the different content in the first row
            content_keys = content_worksheet.row_values(1)
            content_message = (
                f"This Continent can be chosen to visit: "
                + f"\n "
                + f"\n{t.cyan}{t.bold}"
                + " - ".join(content_keys)
            )
            print(content_message)
            print(" ")
            user_content = validation_user_input(
                f"{t.end}What continent in the world are you interested"
                " in?\nChoose a content and press"
                f" {t.bold}{t.underline}ENTER:{t.end} ",
                content_message,
            )
            key_value = user_content

            print(
                "This countries can be choosen in the content"
                f" {t.cyan}{t.bold}{user_content}{t.end}"
            )
            print(" ")
            if user_content in key_value:
                # 1. Creating another variabel for displaying all the
                # worksheets first row values
                # "africa","america","asia","europa"
                first_row_values = content_worksheet.row_values(1)
                # 2. Creating another variabel for checking our first row
                # values for the key heading variabel we are searching for. We
                # use + 1 becouse the first column are [0]
                column_index = first_row_values.index(key_value) + 1
                # 3. We create another variabel that will be assigned the first
                # column and all that values that are in the same column, in
                # this case "Africa".
                column_values = content_worksheet.col_values(column_index)
                # 4. Using a loop, we iterate through each value in
                # column_values, printing each value to the terminal.
                for value in column_values:
                    print(f"{t.cyan}{t.bold}{value}{t.end}")
            print(" ")
            user_country = validation_user_input(
                "What country in the wonderful continent of"
                f" {t.cyan}{t.bold}{user_content}{t.end} would you like to"
                " visit?\nChoose a country and press"
                f" {t.bold}{t.underline}ENTER:{t.end} ",
                column_values,
            )
            user_saved_data = press_enter_to_continue(
                "You have been choosing"
                f" {t.cyan}{t.bold}{user_content}{t.end} and country"
                f" {t.cyan}{t.bold}{user_country}{t.end}. Great"
                f" choice!\nType {t.bold}{t.underline}ENTER{t.end} to see"
                " what currency that are used in that country!"
            )
            print("Please wait for the currency to load...")
            # Declaring variabel from the worksheet that can be used in the
            # code below
            currency_worksheet = SHEET.worksheet("currency")
            # Get the value of the first cell in the first row which contain
            # "country".
            key_value = currency_worksheet.col_values(1, 1)
            # Get the total number of rows in the worksheet.
            num_rows = len(currency_worksheet.col_values(1))

            # Flag to check if the user_country is found in the worksheet.
            found = False

            # Iterate over the rows starting from the second row (index 1).
            for i in range(1, num_rows):
                # Get the value of the cell in the current row and the country
                # column.
                country = currency_worksheet.cell(i, 1).value

                if country == user_country:
                    found = True
                    row_values = currency_worksheet.row_values(i)
                    print(
                        "In the country"
                        f" {t.cyan}{t.bold}{user_country}{t.end} they are"
                        " using the currency\n"
                        + f"\n"
                        + f"{t.cyan}{t.bold}"
                        + " - ".join(row_values)
                    )
                    break
            if not found:
                print("Country not found.")
            print(" ")
            print(
                f"{t.end}If you do not have this currency,\nwe recommend"
                f" you to go to our {t.cyan}{t.bold}Exchange"
                f" service{t.end} in the main menu!"
            )
            print(" ")
        except APIError as e:
            error_message = (
                f"{t.red}An error occurred while accessing the server: Too"
                " many requests per minute.\nPlease wait 25sec! Go back"
                " to the main menu and check out other stuff in the"
                f" meantime!{t.end}"
            )
            print(error_message)
        while True:
            repeat_input = input(
                "Do you wanna try another travel destination? Type"
                f" ({t.bold}{t.green}Y{t.end}) and press"
                f" {t.bold}{t.underline}ENTER{t.end}\nGo back to main"
                f" menu? Type {t.end}({t.bold}{t.red}N{t.end}) and press"
                f" {t.bold}{t.underline}ENTER{t.end} \n"
            ).upper()
            if "N" not in repeat_input and "Y" not in repeat_input:
                print(
                    f'{t.red}Please press either "Y" for YES or "N" for'
                    f' NO{t.end}'
                )
            if "Y" in repeat_input:
                os.system("clear")
                display_menu_country_title()
                break
            elif "N" in repeat_input:
                os.system("clear")
                welcome_menu(user_name)
                break
            else:
                continue


# Alternative 2 in menu - Country Currency Code
def display_menu_currency_code(user_name):
    """
    Will display the correct currency code,
    if user doesnt know the correct 3 letter code
    """
    display_menu_currency_code_title()
    print(
        "Here you will find a list with all 3 Letters codes and country!"
        f" \nBe sure to scroll {t.bold}up{t.end} and"
        f" {t.bold}down{t.end} to get full overview over the list!\n"
    )
    print("Loading the list, please wait")
    time.sleep(4)
    print(" ")
    print(" ")
    print(f"{t.bold}Checkout the list below:{t.end}")
    print(" ")
    for key, value in currency_dict.items():
        print(
            f"Code: {t.cyan}{t.bold}{key}{t.end} Country:"
            f" {t.cyan}{t.bold}{value}{t.end}"
        )
        print("------------------")
    while True:
        repeat = input(
            "Go back to main menu, Press"
            f" {t.bold}{t.underline}ENTER{t.end}\n"
        ).upper()
        if repeat == "":
            os.system("clear")
            welcome_menu(user_name)
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
                f"{t.red}Name should contain least 3 letters and you gave"
                f" us {len(name)}!{t.end}"
            )
        for letter in name:
            if not letter.isalpha():
                raise ValueError(
                    f"{t.red}We can only accept letters from A to"
                    f" Z.{t.end}"
                )
    except ValueError as e:
        print(f"{t.red}Obs!{t.end} {e} {t.red}Try again!{t.end}\n")
        return False
    return True


def validate_number(number, min_option, max_option):
    """
    Validates that user is putting an integer within the specified range.
    """
    while True:
        try:
            userInput = int(input(number))
            if min_option <= userInput <= max_option:
                return userInput
            else:
                print(
                    f"{t.red}Invalid option. Please choose a number"
                    f" between {min_option} and {max_option}.{t.end}"
                )
        except ValueError:
            print(
                f"{t.red}Invalid input. Please enter a valid"
                f" number.{t.end}"
            )


def validation_user_input(question, valid_values):
    """
    Checks and compares the user input to the valid values
    Values are a countries and codes
    """
    while True:
        # Remove leading/trailing spaces
        user_input = input(question).capitalize().strip()
        if user_input == "" or user_input.isdigit():
            print(f"{t.red}Please enter a valid input.{t.end}")
        elif user_input not in valid_values:
            print(
                f"{t.red}Sorry, the content you entered is not in the list"
                f" above. Try again.{t.end}"
            )
        else:
            return user_input


def press_enter_to_continue(enter_prompt):
    """
    Checks and compares the user input to the valid value
    This value are ENTER or enter string
    """
    while True:
        user_input = input(enter_prompt)
        if user_input.lower() == "enter":
            break
        else:
            print(
                f"{t.red}Please type exactly 'ENTER' and press Enter."
                f" {t.end} \n"
            )


def main():  # Main Start Function
    """
    Will run all everything
    """
    user_name = welcome_message()
    welcome_menu(user_name)


main()
