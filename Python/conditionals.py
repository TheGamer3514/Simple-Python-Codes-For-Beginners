
"""
conditionals.py
Asks the user for a number and checks if it is even or odd.
"""

def check_even_odd():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

check_even_odd()
