# Exercise 8.1 - Check Protection

# David Vance
# Professor Kevin Chang
# CIS129 - Programming and Problem Solving I

"""This program prompts the user for a dollar amount in numeric form, verifies
the data fits the program's format, then prints the dollar amount in check-
protected format."""

# INITIALIZING
# Import libraries, set constant values, and define functions

BANNER = 'WELCOME TO CHECK PROTECTION FORMATTER'


def display_banner():
    """This module displays the Welcome Banner"""

    # Display Welcome Banner
    print(f'{BANNER:^60}') # Center-justifies banner for 60 spaces
    
    return


def is_float(check_amount):
    """This module checks to confirm that the string value is in float format."""
    
    try:
        float(check_amount)
        return True
    except ValueError:
        return False


def input_check_amount():
    """This module prompts the user to enter the value of the check in
    dollars and cents."""

    check_amount = input('Please enter the amount of the check in dollars and cents format: ')
    
    while not is_float(check_amount):
        print('You entered an incorrect value.  Please try again.')
        check_amount = input('Please enter the amount of the check in dollars and cents format.')

    check_amount = float(check_amount)

    return check_amount


def display_check_protected_format(check_amount):
    """This module displays the check in protected format:
    - right-justified
    - to 2 decimal points
    - with preceding asterisks
    - to a total of 10 digits."""

    print('Your check amount in protected format: ', end = '')
    print(f'${check_amount:*>10.2f}')
    print('\n')


def main():
    """This module prints the welcome banner, calls to have the check amount
    input, then calls the output banner."""

    display_banner()
    
    check_amount = input_check_amount()

    display_check_protected_format(check_amount)


# BEGIN MAIN PROCESSING

main()

