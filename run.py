'''
Travel Guide - Currency Converter
-------------------------------------------------------------
Made by: Kim Bergstroem
'''
import sys, time, os, requests, gspread
import time
from google.oauth2.service_account import Credentials
from modules.converter import display_meny_exchange
from modules.ascii_art import display_welcome_title, display_welcome_meny, display_meny_country_title # Adds ascii art text headings
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
        user_input_int = validate_number(f"Please {t.green}{t.bold}{user_name}{t.end}, Enter your number here and press {t.bold}{t.underline}ENTER{t.end}: ")            
        if user_input_int == 1:
            os.system('clear')
            display_meny_country(user_name)
            break
        elif user_input_int == 2:
            display_meny_currency_code()
            break
        elif user_input_int == 3:
            os.system('clear')
            if not display_meny_exchange():
                return  # Return to the main menu
            os.system('clear')
        elif user_input_int == 4:
            print(" ")
            print(f"Thank you {t.green}{t.bold}{user_name}{t.end} for this time!" )
            print(f"I Hope you enjoyed this {t.green}{t.bold}Travel Guide{t.end}! I will see you next time!!{t.end}" )
            time.sleep(6)
            os.system('clear')
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

    LINE_UP = '\033[1A'     # Module Time function, Move up n(=1) lines
    LINE_CLEAR = '\x1b[2K'  # Module Time function, Erase current line

    currency_worksheet = SHEET.worksheet("currency")    # Declaring variabel from the worksheet that can be used in the code below
    content_worksheet = SHEET.worksheet("content")      # Declaring variabel from the worksheet that can be used in the code below
    content_keys = content_worksheet.row_values(1)      # Which display the different content in the first row

    #PRINT OUT THE CONTENTS
    display_meny_country_title()
    print(f"{t.bold}Let us help you decide were to travel with a small questionare!{t.end} ")
    time.sleep(5)
    print(LINE_UP, end=LINE_CLEAR)
    print(f"{t.bold}Where do YOU want to travel? {t.red}{t.bold}Warm{t.end} {t.bold}or {t.blue}{t.bold}Cold{t.end}{t.bold} weather? City or Island?{t.end} ")
    time.sleep(5)
    print(LINE_UP, end=LINE_CLEAR)
    while True:
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
        user_saved_data = input(f"You have been choosing {t.cyan}{t.bold}{user_content}{t.end} and country {t.cyan}{t.bold}{user_country}{t.end}. Great choice!\nPress {t.bold}{t.underline}ENTER{t.end} to see what currency that are used in that country!")

        key_value = currency_worksheet.col_values(1, 1)   # Get the value of the first cell in the first row (assuming it contains "country").
        num_rows = len(currency_worksheet.col_values(1))  # Get the total number of rows in the worksheet.

        found = False  # Flag to check if the user_country is found in the worksheet.

        # Iterate over the rows starting from the second row (index 1).
        for i in range(1, num_rows):
            country = currency_worksheet.cell(i, 1).value # Get the value of the cell in the current row and the country column.

            if country == user_country:
                found = True
                row_values = currency_worksheet.row_values(i)
                print(f"In the country {t.cyan}{t.bold}{user_country}{t.end} they are using the currency\n" + f"\n" + f"{t.cyan}{t.bold}" + " - ".join(row_values))
                break
        if not found:
            print("Country not found.")
        print(" ")
        print(f"{t.end}If you do not have this currency, we recommend you to go to our exchange service in the main menu!")

        while True:
            repeat_input = input(f"Do you wanna try another travel destination? Type ({t.bold}{t.green}Y{t.end}) and press {t.bold}{t.underline}ENTER{t.end}\nGo back to main menu? Type {t.end}({t.bold}{t.red}N{t.end}) and press {t.bold}{t.underline}ENTER{t.end} \n").upper()
            if "N" not in repeat_input and "Y" not in repeat_input:
                print(f'{t.red}Please press either "Y" for YES or "N" for NO{t.end}')
            if "Y" in repeat_input:
                os.system('clear')   
                display_meny_country_title()                
                break
            elif "N" in repeat_input:
                os.system('clear')
                welcome_meny(user_name)
                break
            else:
                continue

def display_meny_currency_code(): # Alternative 2 in meny - Country Currency Code
    """
    Will display the correct currency code, if user doesnt know the correct 3 letter code
    """
    print("Here you have a list of all country currency codes that you can use for exchange")
    welcome_meny()


'''
################### Validation functions #########################
'''
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

def validation_user_input(question, valid_values):
    """
    Checks and comparing to the worksheet values, keys if user picks right value
    """
    while True:
        user_input = input(question).capitalize()
        if user_input == "":
            print(f"{t.red}Please enter a valid input.{t.end}")
        elif user_input.isnumeric():
            print(f"{t.red}Please enter a valid input, not a number.{t.end}")
        elif user_input and user_input in valid_values:
            return user_input
        else:
            print(f"{t.red}Sorry, the content you entered is not in the list above. Try again.{t.end}")


def main(): # Main Start Function
    """
    Will run all everything
    """
    user_name = welcome_message()
    welcome_meny(user_name)

main()
