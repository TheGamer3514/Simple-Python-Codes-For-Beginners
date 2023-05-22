type1 = "C"

type2 = "F"

type = input("Enter the letter of the temperature you wish to convert (C or F):")

temp = int(input("Enter the temperature value:"))

if type == type1:

  answer = str((temp * 1.8) + 32)
  
  print ("In Fahrenheit this is: " + answer)

if type == type2:

  answer = str((5/9 * (temp-32)))

  print ("In Celsius this is: " + answer)

if type != type1 and type != type2:

   print ("You have entered an incorrect temperature type")
