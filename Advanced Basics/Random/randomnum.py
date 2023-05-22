import random
lowest = int(input("Enter the lowest number: "))
highest = int(input("Enter the highest number: "))
randomnum = random.randint(lowest,highest)
print("The random number is " + str(randomnum))
