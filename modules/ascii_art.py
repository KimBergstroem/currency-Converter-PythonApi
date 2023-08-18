'''
Different ASCII HEADINGS TEXT
-------------------------------------------------------------
'''
from modules.text_colors import TextColors
t = TextColors


def display_welcome_title():  # Welcome Title
    welcome_title = f"""
 {t.yellow}

 _____________________________________________________________________
  _____                    _    ____       _     _                    |
 |_   _| __ __ ___   _____| |  / ___|_   _(_) __| | ___               |
   | || '__/ _` \ \ / / _ \ | | |  _| | | | |/ _` |/ _ |              |
   | || | | (_| |\ V /  __/ | | |_| | |_| | | (_| |  __/              |
   |_||_|  \__,_| \_/ \___|_|  \____|\__,_|_|\__,_|\___|              |
 {t.magenta}                                                                     |
   __          _                                                      |
  /__\_  _____| |__   __ _ _ __   __ _  ___                           |
 /_\ \ \/ / __| '_ \ / _` | '_ \ / _` |/ _ |                          |
//__  >  < (__| | | | (_| | | | | (_| |  __/                          |
\__/ /_/\_\___|_| |_|\__,_|_| |_|\__, |\ {t.bold}Made by Kim B{t.end}{t.magenta}                |
                                 |___/   {t.bold} github.com/KimBergstroem{t.end}{t.magenta}    | {t.end}                  
    """
    print(welcome_title)


def display_welcome_menu():  # Welcome Menu
    welcome_menu = f"""  
 {t.yellow}
 _____________________________________________________________________
                                                                      |
  /\/\   ___ _ __  _   _                                              |
{t.yellow} /    \ / _ \ '_ \| | | |{t.end}       {t.magenta}{t.bold}1. Country tips{t.end}{t.yellow}                       |
/ /\/\ \  __/ | | | |_| |{t.end}       {t.magenta}{t.bold}2. Currency codes{t.end}{t.yellow}                     |
\/    \/\___|_| |_|\__, |{t.end}       {t.magenta}{t.bold}3. Exchange service{t.end}{t.yellow}                   |
                   |___/{t.end}        {t.magenta}{t.bold}4. Quit{t.end}{t.yellow}                               |
                                                                      |
{t.bold}Enter the number of the navigation menu{t.end}{t.yellow}                               |                                            
    {t.end}"""
    print(welcome_menu)


def display_menu_exchange_title():  # Exchange Menu Title
    exchange_title = f"""  
 {t.yellow}
 _____________________________________________________________________
   __          _{t.end}                                       {t.green}_{t.end}          {t.yellow}    |
  /__\_  _____| |__   __ _ _ __   __ _  ___{t.end}           {t.green}| |{t.end}         {t.yellow}    |
 /_\ \ \/ / __| '_ \ / _` | '_ \ / _` |/ _ |{t.end}         {t.green}/ __){t.end}        {t.yellow}    |
//__  >  < (__| | | | (_| | | | | (_| |  __/{t.end}         {t.green}\__ \{t.end}        {t.yellow}    |
\__/ /_/\_\___|_| |_|\__,_|_| |_|\__, |\___|{t.end}         {t.green}(   /{t.end}        {t.yellow}    |
                                 |___/{t.end}                {t.green}|_|{t.end}         {t.yellow}    | 
                                                                      |
{t.bold}Convert your current currency into another one{t.end}                    {t.yellow}    |                
  {t.end}                                                         
    """
    print(exchange_title)


def display_menu_country_title():  # Exchange Menu Title
    country_title = f"""  
 {t.yellow}
 _____________________________________________________________________
   ___                  _                     {t.green}___   ____{t.end}              {t.yellow}|
  / __\___  _   _ _ __ | |_ _ __ _   _      {t.green}/' --;^/ ,-_\{t.end}     {t.yellow}\ | /   |
 / /  / _ \| | | | '_ \| __| '__| | | |    {t.green}/ /--o\ o-\ \ \{t.end}   {t.yellow}--(_)--  |
/ /__| (_) | |_| | | | | |_| |  | |_| |   {t.green}/-/-/|o{t.end}{t.white}|-|{t.end}{t.green}\-\-\|\   {t.yellow}/ | \   |
\____/\___/ \__,_|_| |_|\__|_|   \__, |    {t.green}'`  `{t.end}{t.white} |-|{t.end}{t.green}   `` '{t.end} {t.yellow}          |
                                 |___/           {t.white}|-|{t.end}                  {t.yellow}|
                                                 {t.white}|-|{t.end}                  {t.yellow}|
{t.bold}Best Travel Guide 2023{t.end}                                            {t.yellow}    |                
  {t.end}                                                         
    """
    print(country_title)


def display_menu_currency_code_title():  # Exchange Menu Title
    currency_title = f"""  
 {t.yellow}
 _____________________________________________________________________
   ___          _          {t.magenta}__ _ _{t.end}                                     {t.yellow}|
  / __\___   __| | ___    {t.magenta}/ /(_) |__  _ __ __ _ _ __ _   _{t.end}            {t.yellow}|
 / /  / _ \ / _` |/ _ \  {t.magenta}/ / | | '_ \| '__/ _` | '__| | | |{t.end}           {t.yellow}|
/ /__| (_) | (_| |  __/ {t.magenta}/ /__| | |_) | | | (_| | |  | |_| |{t.end}           {t.yellow}|
\____/\___/ \__,_|\___| {t.magenta}\____/_|_.__/|_|  \__,_|_|   \__, |{t.end}           {t.yellow}|
                                                     {t.magenta}|___/{t.end}            {t.yellow}|
{t.bold}List of codes / country{t.end}                                               {t.yellow}|                
  {t.end}                
    """
    print(currency_title)
