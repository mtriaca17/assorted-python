import random

random_num = random.randint(1,10)
tries = 0 
end_condition = False
user_name = input("hello please enter a username. ")

def game_guess():
	global end_condition, tries, random_num

	while end_condition != True:
		# print(random_num)
		guess = int(input("Guess: "))
		tries +=1
		if guess == random_num:
			end_condition = True
		elif guess < random_num:
			print("Higher")
		elif guess > random_num:
			print("lower")
	print("GAME END!")
print("hello "+user_name)

question = input("Would u like to play a game? [Y/N]")
number = 2
while question.lower() not in("y", "n"):
	question = input("enter y or n only!: " )
	# print("input was ", question)
if question.lower() == "n":
	print("bye then!")
if question.lower() =="y":
	print("im thinking of a number between 1 and 10")
	game_guess()
	print("GRATS U WON! \nTRIES: {}!".format(tries))
try_again = input("Do u wanna try again?[Y/N] ")
while try_again.lower() not in("y", "n"):
	try_again = input("enter y or n only!: ")
if try_again.lower() == "n":
	print("ok bye!")
	exit()
if try_again.lower() == "y":
	tries = 0
	end_condition = False
	random_num = random.randint(1,10)
	print("ok go again!")
	game_guess()
	print("GRATS U WON AGAIN! \nTRIES {}!".format(tries))





