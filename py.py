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
    # user_content = input("What content in the world are you interested to travel to?")
    # user_country = input("What country in this {user_content} would you like to visit?")
    # DISPLAY LATER ON THE USER VALUE INPUT AND COMPARE TO THE LIST AND THEN DISPLAY THE CURRENCY.

    #PRINT OUT THE CONTENTS
    content_worksheet = SHEET.worksheet("content")
    content_values = content_worksheet.row_values(1) #Which display the different content in the first row
    content_message = (f"This Content can be chosen to visist:\n{t.cyan}{t.bold}" + " - ".join(content_values))
    print(content_message)


    # #PRINT OUT THE COUNTRIES IN THAT CONTENT
    # region_worksheet = SHEET.worksheet("content")             # 1. Create variabel to link with the worksheet with name "region" in the excel file online
    # key_value = "Africa"                                      # 2. The value of the key heading in the excel file inside of the worksheet "region".
    # first_row_values = region_worksheet.row_values(1)         # 3. Creating another variabel for displaying all the worksheets first row values "africa","america","asia","europa"
    # column_index = first_row_values.index(key_value) + 1      # 4. Creating another variabel for checking our first row values for the key heading variabel we are searching for. We use + 1 becouse the first column are [0]
    # column_values = region_worksheet.col_values(column_index) # 5. We create another variabel that will be assigned the first column and all that values that are in the same column, in this case "Africa".
    # print("This countries can be choosen in the content Africa:")                  # 6. Regulare print statement for fun :)
    # for value in column_values:                               # 7. Using a loop, we iterate through each value in column_values, printing each value to the terminal.
    #     print(value)                                          # 8. Each value is printed one by one.






def main(): # Main Start Function
    """
    Will run all everything
    """
    display_meny_country()
main()