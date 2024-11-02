"""
findMax.py
This script finds the maximum number in a list of user-provided numbers.
"""

def find_max(numbers):
    """Function to find the maximum number in a list."""
    max_number = numbers[0]  # Assume the first number is the maximum
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

# Get user input
user_input = input("Enter numbers separated by spaces: ")
numbers_list = list(map(int, user_input.split()))

# Find the maximum number
maximum = find_max(numbers_list)

# Display the result
print("The maximum number is:", maximum)
