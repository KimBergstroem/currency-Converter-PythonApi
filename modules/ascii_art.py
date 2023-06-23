'''
Different ASCII HEADINGS TEXT
-------------------------------------------------------------
'''
from modules.text_colors import TextColors
t = TextColors

def display_welcome_title(): # Welcome Title
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
\__/ /_/\_\___|_| |_|\__,_|_| |_|\__, |\___|                          |
                                 |___/   {t.bold}Made by  Kim B{t.end}{t.magenta}               |                   
  {t.end}                                                         
    """
    print(welcome_title)


def display_welcome_meny(): # Welcome Meny
    welcome_meny = f"""  
 {t.yellow}
 _____________________________________________________________________
                                                                      |
  /\/\   ___ _ __  _   _                                              |
{t.yellow} /    \ / _ \ '_ \| | | |{t.end}       {t.magenta}{t.bold}1. Country{t.end}{t.yellow}                            |
/ /\/\ \  __/ | | | |_| |{t.end}       {t.magenta}{t.bold}2. Currency code{t.end}{t.yellow}                      |
\/    \/\___|_| |_|\__, |{t.end}       {t.magenta}{t.bold}3. Exchange{t.end}{t.yellow}                           |
                   |___/{t.end}        {t.magenta}{t.bold}4. Quit{t.end}{t.yellow}                               |
                                                                      |
{t.bold}Enter the number of the navigation meny{t.end}{t.yellow}                               |                                            
    {t.end}"""
    print(welcome_meny)


def display_meny_exchange_title(): # Exchange Meny Title
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


def display_meny_country_title(): # Exchange Meny Title
    country_title = f"""  
 {t.yellow}
 _____________________________________________________________________
   ___                  _                     ___   ____              |
  / __\___  _   _ _ __ | |_ _ __ _   _      /' --;^/ ,-_\     \ | /   |
 / /  / _ \| | | | '_ \| __| '__| | | |    / /--o\ o-\ \ \   --(_)--  |
/ /__| (_) | |_| | | | | |_| |  | |_| |   /-/-/|o|-|\-\-\|\   / | \   |
\____/\___/ \__,_|_| |_|\__|_|   \__, |    '`  ` |-|   `` '           |
                                 |___/           |-|                  |
                                                 |-|                  |
{t.bold}Best Travel Guide 2023{t.end}                                            {t.yellow}    |                
  {t.end}                                                         
    """
    print(country_title)
