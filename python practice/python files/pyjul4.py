#functions
# def greet_user(username):
#     """DOSCTRING described what function does, prints hello username"""
#     print(f'Hello, {username.title()}.')

# user = input('What is your username?? ')

# greet_user(user)

#positional arguments
# def describe_pet(animal_type, name):
#     """info about pet"""
#     print(f'I have a {animal_type} and his name is {name.title()}.')

# describe_pet('dog', 'gibbs')
# describe_pet('dog', 'ducky')

#keyword arguments
# def describe_pet(animal_type, name):
#     """info about pet"""
#     print(f'I have a {animal_type} and his name is {name.title()}.')

# describe_pet(animal_type = 'dog', name = 'gibbs')
# describe_pet('dog', 'ducky')

#default values can be added
# def describe_pet(name, animal_type='dog'):
#     """info about pet"""
#     print(f'I have a {animal_type} and his name is {name.title()}.')

# describe_pet('gibbs')
# describe_pet('jefferson', 'rabbit')#adding arguments overrules the default

# def get_formatted_name(first_name, last_name):
#     """return full name"""
#     full_name = f'{first_name} {last_name}'
#     return full_name.title()
# formatted_name = get_formatted_name('miguel', 'triaca')
# print(formatted_name)

#making a parameter optional

# def get_formatted_name(first_name, last_name, middle_name =''):
#     """return full name"""
#     if middle_name: #non empty strings are interpreted as True
#         full_name = f'{first_name} {middle_name} {last_name}'
#     else:
#         full_name = f'{first_name} {last_name}'
#     return full_name.title()
# formatted_name = get_formatted_name('miguel', 'triaca')
# print(formatted_name)
# formatted_name_2 = get_formatted_name('tim', 'lee', 'berners')
# print(formatted_name_2)

#returning a dict
# def build_person(first_name, last_name, age=''):
#     """return dict about a person"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# loyal_player = build_person('demar', 'derozan', age= 28)
# print(loyal_player)

# def get_formatted_name(first_name, last_name):
#     """return full name"""
#     full_name = f'{first_name} {last_name}'
#     return full_name.title()

# while True:
#     print('\nWhat is your name? ')
#     print('(enter q at any time to quit)')

#     f_name = input('First Name: ')
#     if f_name == 'q':
#         break
    
#     l_name = input('Last Name: ')
#     if l_name == 'q':
#         break
    
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f'\nHello {formatted_name}')

#     ask_quit = input('Press q to quit')
#     if ask_quit:
#         break

#  passing a list to a function
# def greet_users(names):
#     """print greeting for each user"""
#     for name in names: 
#         msg = f'Hello, {name.title()}!'
#         print(msg)
# usernames = ['gibbs', 'ducky', 'migs']
# greet_users(usernames)

#modifying lists in functions

# unprinted_designs = ['iphone', 'robot','dodecahedron']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()

#     print(f'Printing model: {current_design}')
#     completed_models.append(current_design)

# print('\nThe following have been completed: ')
# for completed_model in completed_models:
#     print(completed_model)
# #above code can be reorganized with functions

# def print_models(unprinted_designs, completed_models):
#     """sim print until nothing left then move to other array"""
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()

#         print(f'\nprinting {current_design}')
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """print all finished"""
#     print('\nTHe following have been done:')

#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['closet', 'kitchen', 'room']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

#preventing a funciton from modifying a list
# def print_models(unprinted_designs, completed_models):
#     """sim print until nothing left then move to other array"""
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()

#         print(f'\nprinting {current_design}')
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """print all finished"""
#     print('\nTHe following have been done:')

#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['closet', 'kitchen', 'room']
# completed_models = []
# print_models(unprinted_designs[:], completed_models)#adding slice makes it take a copy of the list
# show_completed_models(completed_models)
# print(unprinted_designs)


#exercises
# def show_magicians(names):
#     for name in names:
#         print(f'Hello {name} the magician!')

# # def make_great(names):#shortcut solution to the below code
# #     for i, name in enumerate(names):
# #         names[i] = name +" the great!"

# def make_great(names):
#     great_magicians = [] #hold the new strings

#     while names:
#         new_name = names.pop()
#         great_magician = new_name + ' the Great'
#         great_magicians.append(great_magician)     

#     for great_magician in great_magicians:
#         names.append(great_magician)
    
#     return names

# magicians_names = ['bob', 'steven','zantana']
# print('original magicians: ')
# show_magicians(magicians_names)

# great_magicians = make_great(magicians_names[:])
# print('\nGreat Magicians: ')
# show_magicians(great_magicians)

#arbitrary number of arguments
# def make_pizza(*toppings):
#     """print list of toppings that have been requested"""
#     print('\nMaking a a pizza with the toppings: ')
#     for topping in toppings:
#         print(f'- {topping}')
# make_pizza('pepperoni')
# make_pizza('cheese', 'jalapeno','sasuage')

#can be mixed with positional 
# def make_pizza(size, *toppings):
#     """print list of toppings that have been requested"""
#     print(f'\nMaking a {size} inch pizza with the toppings: ')
#     for topping in toppings:
#         print(f'- {topping}')
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'cheese', 'jalapeno','sasuage')

#arbitary keyword arugments
# def build_profile(first, last, **user_info):
#     """building profile of user"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for k, v in user_info.items():
#         profile[k] = v
#     return profile

# user_profile = build_profile('gibbs', 'the dog', location = 'makati', field = 'physics')
# print(user_profile)

#importing from a module
# import pizza as pz
# pz.make_pizza(16, 'anchovy', 'pepperoni')

#importing just a function(can also give alias to function)
# from pizza import make_pizza as mp
# mp(16, 'anchovy','pepperoni')

#importing all functions from a module
# from pizza import *

# make_pizza(16, 'peppers','onions')
