speed = int(input("enter hurricane speed: "))
if speed >= 157:
  category = "Five" 
elif speed <= 130 or 156:
  category = "Four" 
elif speed <= 111 or 129:
 category = "Three" 
elif speed <= 96 or 110: 
 category = "Two"
elif speed <= 74 or 95:
  category = "One"
elif speed <= 73:
  category = "Windy"
print("the speed is category:",str(category))
