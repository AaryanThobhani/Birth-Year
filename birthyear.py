# Program for getting the year of birth
# By Aaryan Thobhani
# GitHub:  https://github.com/AaryanThobhani

# Importing Libs
from datetime import date

# Variables
today = date.today()

user_input_yes = input("Is your birthday in {} celebrated yet? (Yes or No) :".format(today.year))

user_input = input("How old are you?:")

birth_year = int(today.year) - int(user_input)


# If and else Statements
if user_input_yes == "Yes":
    print("You are {} years old, and you were born in {}.".format(int(user_input), int(birth_year)))
else:
    print("You are {} years old, and you were born in {}.".format(int(user_input), int(birth_year - 1)))


# End of Program

