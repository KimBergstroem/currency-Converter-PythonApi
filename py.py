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




def display_meny_country(): # Alternative 1 in meny - Country Display
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
    while True:
        print(f"{t.bold}Let us help you decide were you want to travel with a small questionare!{t.end} ")
        time.sleep(5)
        print(LINE_UP, end=LINE_CLEAR)
        print(f"{t.bold}Where do you WANT to travel to? What content? {t.red}{t.bold}Warm{t.end} {t.bold}or {t.blue}{t.bold}Cold{t.end}{t.bold} weather? City or Island?{t.end} ")
        time.sleep(5)
        print(LINE_UP, end=LINE_CLEAR)
        content_message = (f"This Content can be chosen to visit: " + f"\n " + f"\n{t.cyan}{t.bold}" + " - ".join(content_keys))
        print(content_message)
        print(" ")
        user_content = validation_user_input(f"{t.white}What content in the world are you interested in? Choose a content and press {t.bold}{t.underline}ENTER:{t.end} ", content_message)

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
        user_country = validation_user_input(f"What country in the wonderful content {t.cyan}{t.bold}{user_content}{t.end} would you like to visit?\nChoose a country and press {t.bold}{t.underline}ENTER:{t.end} ", column_values)
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
                print(f"In the country {t.cyan}{t.bold}{user_country}{t.end} they are using the currency " + f"\n{t.cyan}{t.bold}" + " - ".join(row_values))
                break
        if not found:
            print("Country not found.")
        print(f"{t.end}If you do not have this currency, we recommend you to go to our exchange currency in the main meny!")

        while True:
            repeat_input = input(f"Do you wanna try another travel destination? ({t.green}y{t.end}) OR Go back to main meny? ({t.red}n{t.end}): \n").upper()
            if "N" not in repeat_input and "Y" not in repeat_input:
                print(f"Please press either {t.green}y{t.end} or {t.red}n{t.end}")
            if "Y" in repeat_input:
                os.system('clear')
                display_meny_country()
                break
            elif "N" in repeat_input:
                os.system('clear')
                welcome_meny(user_name)
                break
            else:
                continue
           



def validation_user_input(question, valid_values):
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
    display_meny_country()
main()