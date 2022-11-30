import random
num1 = random.randint (1,10) 
num2 = random.randint (1,10)
score = 0 
count = 0
computer = num1 * num2 
print("What Is",  str(num1), "X", str(num2),"?")
guess = int(input("Enter Your Answer: "))
if computer == guess: 
	print("Correct Answer")
	score +=1 
else:
	print("This is incorrect, the answer is " + str(computer))
