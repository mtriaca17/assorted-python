# prompt = input('input something:\n')
# print(prompt)
# name_message = input('What is your name?\n')
# print('Hello', name_message)
# age = input('How old are you? ')

# if int(age) > 18:
# 	print('You are old enough to drink')

# evenodd_check = input('Enter a number and we will check if even or odd: ')
# if int(evenodd_check)%2 == 0:
# 	print(evenodd_check, 'is even!')
# else:
# 	print(evenodd_check, 'is odd!')
#while LOOP 
# current_number = 1
# while current_number <= 5:
# 	print(current_number)
# 	current_number += 1

# prompt = '\nTell me something, and i will repeat it: '
# prompt += '\n Enter \'quit\' to end the program\n'
# user_message =""

# while user_message != 'quit':
# 	user_message = input(prompt)

# 	if user_message != 'quit':
# 		print('\n', user_message)
# active = True
# while active:
# 	message = input(prompt)

# 	if message == 'quit':
# 		active = False
# 	else:
# 		print("REPRINTING message", message)


#break 
# prompt = '\nEnter a city: '
# prompt += '(Enter quit when u r done)'

# while True:
# 	city = input(prompt)

# 	if city == 'quit':
# 		break
# 	else:
# 		print('id like to go to', city.title() +'!')

#continue

# current_num = 0 
# while current_num < 10:
# 	current_num +=1
# 	if current_num % 2 == 0:
# 		continue#skips the even numbers but keeps the loop going
# 	print(current_num)

# for num in range(2,11,2):
# 	print(num)
# prompt = 'What is your age? (enter quit to quit): '

# while True:
# 	age = input(prompt)
# 	if age == 'quit':
# 		break
# 	if int(age)<3:
# 		print('your age is:', age, 'you will pay nothing it is free!')
# 	if int(age) in range(4,13):
# 		print('your age is', age, 'you will pay $10!')
# 	if int(age) > 12:
# 		print('your age is', age, 'you will pay $15!')
# #page 128

#moving items from one list to another

# unconfirmed_users = ['alice', 'bob', 'mario']
# confirmed_users = []

# while unconfirmed_users:
# 	current_user = unconfirmed_users.pop()
# 	print('Verifying User:', current_user.title())
# 	confirmed_users.append(current_user)
# 	# print("Confirmed users now are: ")
# 	# print(*confirmed_users, sep = ', ')
# 	# print(', '.join(confirmed_users))

# animals = ['dog','cat','dog','cat','flareon']
# print(animals)

# while 'cat' in animals:
# 	animals.remove('cat')

# print(animals)

#filling dict with user input
# responses = {}
# polling_active = True

# while polling_active:
# 	name = input('\nWhat is your name? ')
# 	response = input('Which Mountain would you like to climb someday? ')

# 	responses[name] = response

# 	repeat = input('Would you like to let anohter person respond? (yes/no) ')
# 	if repeat == 'no':
# 		polling_active = False

# print('Results: ')
# for name, response in responses.items():
# 	print(name , 'would like to climb', response + '.')
# print(responses)

