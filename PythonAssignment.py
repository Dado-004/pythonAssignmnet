import random

userHand = input("Rock, Paper, or Scissors:")

computerHand = random.random()

if computerHand <= .33:
	computerHand = "Rock"
elif computerHand <= .66:
	computerHand = "Paper"
else:
	computerHand = "Scissors"

def game(first, second):

	if first == second:
		print ("You chose", first)
		print ("Computer chose", second)
		print ("Its a tie.")

	elif first == "Rock":
		if second == "Scissors":
			print ("You chose", first)
			print ("Computer chose", second)
			print ("You win")
		else:
			print ("You chose", first)
			print ("Computer chose", second)
			print ("You lose")

	elif first == "Paper":
		if second == "Rock":
			print ("You chose", first)
			print ("Computer chose", second)
			print ("You win")
		else: 
			print ("You chose", first)
			print ("Computer chose", second)
			print ("you lose")

	elif first == "Scissors":
		if second == "Paper":
			print ("You chose", first)
			print ("Computer chose", second)
			print ("You win")
		else:
			print ("You chose", first)
			print ("Computer chose", second)
			print ("You lose")


game(userHand, computerHand)






