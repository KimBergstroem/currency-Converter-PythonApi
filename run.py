import gspread
from google.oauth2.service_account import Credentials

SCOPE = [ #IAM
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('travel_Guide')

region = SHEET.worksheet('region')

data = region.get_all_values()
print(data)



# TRAVEL GUIDE - CURRENCY EXCHANGE
