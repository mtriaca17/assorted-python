import random
# def reverse(s):
#   reverseString = ""
#   for i in s:
#     reverseString = i + reverseString 
#   print(reverseString)
#   return reverseString

# wordOne = "hello"
# reverse(wordOne)

# age = 23
# message = "Happy "+ str(age)+ "rd birthday!"
# print(message)

pokemon_list = ['totodile', 'charmander', 'treeko']
# print(pokemon_list)
# print(pokemon_list[0].title())

#return the last item
# print(pokemon_list[-1])

#replacing element
pokemon_list[1] = "charizard"
# print(pokemon_list)

#adding element
#append - add to end
pokemon_list.append('feraligatr')
# print(pokemon_list)

#insert
pokemon_list.insert(3, 'pikachu')
# print(pokemon_list)

#removing 
# del pokemon_list[3]
# print(pokemon_list)

#pop - can be used after being removed
# print(pokemon_list)
# popped_pokemon = pokemon_list.pop(2)
# print(pokemon_list)
# print(popped_pokemon)

#remove
# print(pokemon_list.remove('totodile'))
#can also be used with a variable

#ORGANIZING A LIST
#sort method, permanent
# pokemon_list.sort()
# print(pokemon_list)
# pokemon_list.sort(reverse = True)
# print(pokemon_list)

#sorting a list temporarily
# print("original: ", pokemon_list)
# print("sorted: ", sorted(pokemon_list))

#reverse, permanent
# pokemon_list.reverse()
# print(pokemon_list)

#finding length
# print(len(pokemon_list))

#looping through lists
# for pokemon in pokemon_list:
# 	print(pokemon.title() + " is a great pokemon!")

# numbers = list(range(1,6))
# print(numbers)
# even_numbers = list(range(2,11,2))
# print(even_numbers)

# #10 squares print

# squares = []
# for value in range (1,11):
# 	square = value**2
# 	squares.append(square)
# print(squares)
# # above code can be summarized in below code
# squares = [value**2 for value in range(1,11)]
# print(squares)

# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

#SLICING A LIST
celtics_list = ["jaylen brown", "al horford", "jayson tatum", "marcus smart", "kyrie irving"]

# print(celtics_list[0:3])
# print(celtics_list[1:4])
# print(celtics_list[:3])
# print(celtics_list[3:])
# print(celtics_list[1:3])
# print(celtics_list[-2:])

# print("first three players:")
# for celtic in celtics_list [:3]:
# 	print(celtic.title())
# print("last three players:")
# for celtic in celtics_list [-3:]:
# 	print(celtic.title())

# #copying a list
# new_celtics_list = celtics_list[:]
# print(new_celtics_list)

# new_celtics_list.append("daniel theis")
# print(new_celtics_list)

#TUPLES - immutable, cannot be changed
dimensions = (200, 50)
print(dimensions[0])

menu = ('fried chicken', 'roasted chicken', 'baked chicken')

for food_item in menu:
	print(food_item)
# coin flip if practice
# count_head = 0
# count_tails = 0

# for i in range(1,11):
# 	flip = random.randrange(2)

# 	if flip == 0:
# 		print(i, 'heads')
# 		count_head+=1
# 	else:
# 		print(i, 'tails')
# 		count_tails+=1
# print("Count for Heads: {}".format(count_head))
# print("Count for Tails: {}".format(count_tails))
#LEFT OFF AT TESTING MULTIPLE CONDITIONS

# champions = []
# if champions:
# 	print('list is ok')
# else:
# 	print('list is empty')

# champions = ['lebron', 'kyrie', 'curry']

# celtics = ['kyrie', 'hayward', 'smart']

# for champion in champions:
# 	if champion in celtics:
# 		print(champion+' is a celtic')
# 	else:
# 		print(champion+' is not a celtic')

# #page 93 activity
# usernames = ['admin', 'eriksen','modric','rakitic','mandzukic']
# if usernames:
# 	for name in usernames:
# 		if name == 'admin':
# 			print('Hello admin, would you like to see a status report?')
# 		else:
# 			print('Hello', name+ ', thank you for logging in again')
# else:
# 	print('We need to find some users!')

# current_users = usernames
# new_users = ['messi', 'ronaldo', 'MODRIC', 'mandzukic', 'mbappe']

# for user in new_users:
# 	if user.lower() in current_users:
# 		print(user, 'is already in use, you have to enter a new username')
# 	else:
# 		print(user, 'is available!')

# ordinals = list(range(1,10))

# for ordinal in ordinals:
# 	if ordinal in(1,2,3):
# 		if ordinal == 1:
# 			print(str(ordinal)+'st')
# 		elif ordinal == 2:
# 			print(str(ordinal)+'nd')
# 		elif ordinal == 3:
# 			print(str(ordinal)+'rd')
# 	else: 
# 		print(str(ordinal)+'th')
# #ACTIVITY END

#dictonaries
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25 
# print(alien_0)

# alien_1 = {}
# alien_1['color'] = 'blue'
# alien_1['points'] = '5'
# print(alien_1)

# # modifying
# # print("alien is " + alien_0['color'])
# # alien_0['color'] = 'yellow'
# # print('alien color changed to '+ alien_0['color'])
# alien_0['speed'] = 'slow'

# if alien_0['speed'] =='slow':
# 	x_increment = 1
# elif alien_0['speed'] == 'medium':
# 	x_increment = 2
# else:
# 	x_increment = 3

# alien_0['x_position'] += x_increment

# print("New x:", str(alien_0['x_position']))

# # del alien_0['points']
# # print(alien_0)

# favorite_languages = {
# 	'mandzukic': 'python',
# 	'modric': 'c++',
# 	'rakitic': 'go',
# 	'eriksen': 'rubu'
# }

# print('Mandzukic\'s fave language is', favorite_languages['mandzukic'])

#easy dictionary activities
#6-1
# person_1 = {
# 	'first_name' : 'mario',
# 	'last_name' : 'mandzukic',
# 	'nation' : 'croatia'
# }
# print('First Name: {} \nLast Name: {} \nNational Team: {}'.format(person_1['first_name'].title(),person_1['last_name'].title() , person_1['nation'].title()))

# favorite_languages = {
# 	'mandzukic': 'python',
# 	'modric': 'c++',
# 	'rakitic': 'go',
# 	'eriksen': 'ruby'
# }

# # for k, v in favorite_languages.items():
# # 	print('key: {}\nvalue: {}\n'.format(k, v))

# for name, lang in favorite_languages.items():
# 	print(name.title()+'\'s favorite language is ' + lang.title() + '.')

# friends = ['modric', 'rakitic']

# for name in favorite_languages.keys():
# 	print(name.title())

# 	if name in friends:
# 		print( " Hi", name.title() + ', I see your favorite language is', favorite_languages[name].title() +'!')
# for name in sorted(favorite_languages.keys()):
# 	print('{}, thank you for answering'.format(name.title()))
# #printing dict values

# for lang in favorite_languages.values():
# 	print(lang.title())
# # IF THERE ARE DUPLICETS USE set()
# #for example
# footy_teams={
# 	'modric': 'real madrid', 
# 	'ronaldo': 'real madrid',
# 	'rakitic': 'barcelona',
# 	'lewandowski' : 'bayern'
# }
# for teams in footy_teams.values():
# 	print(teams.title())
# # not showing dupes
# for teams in set(footy_teams.values()):
# 	print(teams.title())

# #NESTING
# alien_0 = {'color': 'green', 'points' : 5}
# alien_1 = {'color': 'yellow', 'points' : 10}
# alien_2 = {'color': 'red', 'points' : 15}

# aliens = [alien_0, alien_1, alien_2]
# aliens = []

# for alien_number in range(30):
# 	new_alien = {'color': 'green', 'points' : 5, 'speed': 'slow'}
# 	aliens.append(new_alien)
# print('number of aliens:', len(aliens))

# for alien in aliens[:3]:
# 	if alien['color'] == 'green':
# 		alien['color'] = 'yellow'
# 		alien['points'] = '10'
# 		alien['speed']  = 'medium'
# for alien in aliens[4:7]:
# 	if alien['color'] == 'green':
# 		alien['color'] = 'red'
# 		alien['points'] = '15'
# 		alien['speed']  = 'fast'
# for alien in aliens[:8]:
# 	print(alien)

# pizza = {
# 	'crust' : 'thick',
# 	'toppings' : ['mushrooms', 'anchovies', 'extra cheese'],
# }

# print('You ordered a', pizza['crust'], 'crust pizza with the following topings:')

# for topping in pizza['toppings']:
# 	print("\t"+ topping)


# favorite_languages = {
# 	'eriksen' : ['python', 'ruby'],
# 	'modric' : ['python', 'perl'],
# 	'subasic' : ['go', 'HTML']
# }

# for name, langs in favorite_languages.items():
# 	print('{}\'s favorite languages are:'.format(name.title()))
# 	for language in langs:
# 		print("\t" + language.title())

# # dict of dicts
# users = {
# 	'admin':{
# 		'first': 'migs',
# 		'last' : 'triaca',
# 		'location' : 'bed'
# 	},
# 	'wolfsburg':{
# 	    'first' : 'wolfs',
# 	    'last' : 'burg',
# 	    'location' : 'germany'
# 	}
# }

# for username, user_info in users.items():
# 	print('\nUsername:', username)
# 	full_name = user_info['first'] + " " +user_info['last']
# 	location = user_info['location']
# 	print('\tFull Name: {} \n\tLocation: {}'.format(full_name.title(), location.title()))
# pets = []
# pet0 = {
# 	'name' : 'gibbs',
# 	'color' : 'light brown',
# 	'size' : 'medium',
# 	'cuteness' : 'high',
# }

# pet1 = {
# 	'name' : 'ducky',
# 	'color' : 'dark brown',
# 	'size' : 'small',
# 	'cuteness' : 'high',
# }

# pet2 = {
# 	'name' : 'khikho',
# 	'color' : 'marble',
# 	'size' : 'medium',
# 	'cuteness' : 'high',
# }

# pets = [pet0,pet1,pet2]

# for pet in pets:
# 	print('\nName: {}\nColor: {}\nSize: {}\nCuteness:{}'.format(pet['name'], pet['color'], pet['size'], pet['cuteness']))

# favorite_places= {
# 'migs' : ['room', 'rockwell'],
# 'gibbs' : ['kitchen', 'under bed'],
# 'ducky' : ['under bed', 'chair'],
# }

# for k, v in favorite_places.items():
# 	print('Name:', k.title()+'\nFavorite places:')
# 	for place in v:
# 		print("\t" + place)

cities = {
	'makati' : {
		'population' : '100',
		'country' : 'philippines',
		'fact' : 'nice city'
	},
	'monchengladbach' : {
		'population' : '250',
		'country' : 'Germany',
		'fact' : 'team name is borussia monchengladbach'		
	},
	'vice city' : {
		'population' : '1200',
		'country' : 'fictional america',
		'fact' : 'it is a fictional city'
	}
}

for k, v in cities.items():
	print('Name: { }\nPopulation: {} \nCountry: {} \nFact: {}'.format(k.title(), v['population'],v['country'], v['fact']))