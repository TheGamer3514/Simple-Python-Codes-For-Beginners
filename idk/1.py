unit = input("Enter the unit of the temperature (celsius/fahrenheit): ")

if unit == 'celsius':
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} Celsius is approximately equal to {fahrenheit:.2f} Fahrenheit")
    except ValueError:
        print("Invalid input for temperature!")
elif unit == 'fahrenheit':
    try:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} Fahrenheit is approximately equal to {celsius:.2f} Celsius")
    except ValueError:
        print("Invalid input for temperature!")
else:
    print("Invalid unit selected!")
