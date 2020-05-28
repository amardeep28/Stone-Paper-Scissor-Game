import random
items = ["Paper","Scissor","Stone"]
	
print("\n\t Welcome to Stone Paper Scissor Game...\n")
print(" #RULES")
print("1. Stone breaks Scissor, Scissor cuts Paper, Paper covers Stone")
print("2. You will get 5 chances, for each win you get 10 points")
print("3. One with maximum points wins\n\n")

c = 0
p = 0
i = 0
while (i<5):
	random.shuffle(items)
	comp_choice = random.choice(items)
	
	user_choice = input("Choose your move : 1. for Stone    2. for Paper    3. for Scissor\n")
	
	if user_choice == "1":
		
		if comp_choice == "Stone":
			print("Draw\n")
			i = i + 1
			
		elif comp_choice == "Paper":
			print("You Lose\n")
			i = i + 1
			c = c + 10
			
		elif comp_choice == "Scissor":
			print("You Win\n")
			i = i + 1
			p = p + 10
			
	elif user_choice == "2":
		
		if comp_choice == "Stone":
			print("You Win\n")
			i = i + 1
			p = p + 10
			
		if comp_choice == "Paper":
			print("Draw\n")
			i = i + 1
			
		if comp_choice == "Scissor":
			print("You Lose\n")
			i = i + 1
			c = c + 10
			
	elif user_choice == "3":
		
		if comp_choice == "Stone":
			print("You Lose\n")
			i = i + 1
			c = c + 10
			
		if comp_choice == "Paper":
			print("You Win\n")
			i = i + 1
			p = p + 10
			
		if comp_choice == "Scissor":
			print("Draw\n")
			i = i + 1
			
	else:
	    print("Invalid choice. Try again")
			
print("Your total points: ",p)
print("Computer's total points: ",c)

if p == c :
	print("\nDRAW!\n")
if p>c:
	print("CONGRATULATIONS! YOU WON...\n")
if p<c:
	print("YOU LOSE!\n")
print("\t Thank you for playing !!!")
