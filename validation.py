"""
Travel Guide - Validation file
-------------------------------------------------------------
Made by: Kim Bergstroem
"""
from modules.text_colors import TextColors  # Adds color to text

t = TextColors  # Declaring the function to smaller variabel


def validate_name(name):
    """
    Check if a name contains at least 3 letters and
    consists only of letters (A-Z).

    Args:
        name (str): The name to validate.

    Returns:
        bool: True if the name is valid, False otherwise.
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
    Validates that user inputs an integer within the specified range.

    Args:
        number_prompt (str): The prompt to display to the user.
        min_option (int): The minimum valid value.
        max_option (int): The maximum valid value.

    Returns:
        int: The user's valid input.
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


def validate_user_input(prompt, valid_values):
    """
    Validate user input against a list of valid values.

    Args:
        prompt (str): The prompt to display to the user.
        valid_values (list): A list of valid values for the input.

    Returns:
        str: The user's valid input.
    """
    while True:
        user_input = input(prompt).capitalize()

        if user_input in valid_values:
            return user_input
        elif user_input == "" or user_input.isdigit():
            print(
                f"{t.red}Please enter a valid input"
                f" NOT a number or blank space.{t.end}"
            )
        else:
            print(
                f"{t.red}Sorry, invalid choice."
                f" Please enter one of the options above.{t.end}"
            )


def press_enter_to_continue(enter_prompt):
    """
    Checks and compares the user input to the
    valid value 'ENTER' or 'enter' string.

    Args:
        enter_prompt (str): The prompt to display to the user.

    Returns:
        None
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
