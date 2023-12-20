import random
import string
def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    symbols = string.punctuation
    numbers = string.digits
    password = random.choice(uppercase_letters) + random.choice(lowercase_letters) + random.choice(symbols) + random.choice(numbers)
    remaining_length = length - 4
    password += ''.join(random.choices(uppercase_letters + lowercase_letters + symbols + numbers, k=remaining_length))
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password
length = int(input("Enter the desired password length: "))
password = generate_password(length)
print("Generated password:", password)