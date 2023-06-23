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




def display_meny_country(): # Alternative 1 in meny - Country Display
    """
    Will display all countries in the world and display the currency in that specific country
    Will ask user, were to travel
    """

    LINE_UP = '\033[1A'     # Module Time function, Move up n(=1) lines
    LINE_CLEAR = '\x1b[2K'  # Module Time function, Erase current line

    content_worksheet = SHEET.worksheet("content")   # Declaring variabel from the worksheet that can be used in the code below
    content_keys = content_worksheet.row_values(1) # Which display the different content in the first row
    #content_values = content_worksheet.row_values(1) # Which display the different content in the first row

    #PRINT OUT THE CONTENTS
    print(f"{t.yellow}{t.bold}Let us help you decide were you want to travel with a small questionare!{t.end} ")
    time.sleep(5)
    print(LINE_UP, end=LINE_CLEAR)
    print(f"{t.yellow}{t.bold}Where do you WANT to travel to? What content? Warm or Cold weather? City or Island?{t.end} ")
    time.sleep(5)
    print(LINE_UP, end=LINE_CLEAR)
    content_message = (f"This Content can be chosen to visit: " + f"\n " + f"\n{t.cyan}{t.bold}" + " - ".join(content_keys))
    print(content_message)
    print(" ")
    user_content = input(f"{t.white}What content in the world are you interested in? Choose a content and press {t.bold}{t.underline}ENTER:{t.end} ").capitalize()
    key_value = user_content
    print(f"This countries can be choosen in the content {t.cyan}{t.bold}{user_content}{t.end}") 
    print(" ")
    if user_content in key_value:
        first_row_values = content_worksheet.row_values(1)              # 3. Creating another variabel for displaying all the worksheets first row values "africa","america","asia","europa"
        column_index = first_row_values.index(key_value) + 1            # 4. Creating another variabel for checking our first row values for the key heading variabel we are searching for. We use + 1 becouse the first column are [0]
        column_values = content_worksheet.col_values(column_index)      # 5. We create another variabel that will be assigned the first column and all that values that are in the same column, in this case "Africa".
        for value in column_values:                                     # 7. Using a loop, we iterate through each value in column_values, printing each value to the terminal.
            print(f"{t.cyan}{t.bold}{value}{t.end}") 
    
    print(" ")
    user_country = input(f"What country in the wonderful content {t.cyan}{t.bold}{user_content}{t.end} would you like to visit? Choose a country and press {t.bold}{t.underline}ENTER:{t.end} ").capitalize()






def main(): # Main Start Function
    """
    Will run all everything
    """
    display_meny_country()
main()