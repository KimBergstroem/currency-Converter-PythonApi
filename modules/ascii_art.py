'''
Different ASCII HEADINGS TEXT
-------------------------------------------------------------
'''
from modules.text_colors import TextColors
t = TextColors

def display_welcome_title():
    welcome_title = f"""  
 {t.yellow}

 _________________________________________________________________
  _____                    _    ____       _     _                |
 |_   _| __ __ ___   _____| |  / ___|_   _(_) __| | ___           |
   | || '__/ _` \ \ / / _ \ | | |  _| | | | |/ _` |/ _ |          |
   | || | | (_| |\ V /  __/ | | |_| | |_| | | (_| |  __/          |
   |_||_|  \__,_| \_/ \___|_|  \____|\__,_|_|\__,_|\___|          |
 {t.magenta}                                                                 |
   __          _                                                  |
  /__\_  _____| |__   __ _ _ __   __ _  ___                       |
 /_\ \ \/ / __| '_ \ / _` | '_ \ / _` |/ _ |                      |
//__  >  < (__| | | | (_| | | | | (_| |  __/                      |
\__/ /_/\_\___|_| |_|\__,_|_| |_|\__, |\___|                      |
                                 |___/   Made by  Kim B           |                   
  {t.end}                                                         
    """
    print(welcome_title)


def display_welcome_meny():
    welcome_meny = f"""  
 {t.yellow}
 _________________________________________________________________
                                                                  |
  /\/\   ___ _ __  _   _                                          |
{t.yellow} /    \ / _ \ '_ \| | | |{t.end}       {t.magenta}1. Country{t.end}{t.yellow}                        |
/ /\/\ \  __/ | | | |_| |{t.end}       {t.magenta}2. Currency code{t.end}{t.yellow}                  |
\/    \/\___|_| |_|\__, |{t.end}       {t.magenta}3. Exchange{t.end}{t.yellow}                       |
                   |___/{t.end}        {t.magenta}4. Quit{t.end}{t.yellow}                           |
                                                                  |
{t.bold}Please enter the number of the meny for enter that topic          |
{t.end}                                            
    """
    print(welcome_meny)