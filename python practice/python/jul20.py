# from collections import OrderedDict

# favorite_languages = OrderedDict()

# favorite_languages['jen'] = 'python'
# favorite_languages['santos'] = 'ruby'
# favorite_languages['miguel'] = 'c++'
# favorite_languages['xd'] = 'go'

# for name, lang in favorite_languages.items():
#     print(f'{name.title()}\'s favorite langues is {lang}')

# with open('practicefile.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip()) #rstrip, remove whitespace right of string
 
# filename = 'practicefile.txt'


# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

# filename = 'practicefile.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# string_new = ''
# for line in lines:
#     string_new += line.rstrip()

# birthday = '121796'
# if birthday in string_new:
#     print('Your bday is contained in the string!')
# else:
#     print('your bday is not contianed')

# filename = 'newtext.txt'

# # with open(filename, 'w') as file_object:
# #     file_object.write('i love python\n')
# #     file_object.write('i love it alot')

# with open(filename, 'a') as file_object:
#     file_object.write('i love programming\n')

#Exceptions
#try exceept
#zerodivisionerror
# print('enter 2 numbers. ')
# print('press q to quit bro.')

# while True:
#     first_num = input('\nFirst Number: ')
#     if first_num == 'q':
#         break
#     second_num = input('\nSecond Number: ')
#     if second_num == 'q':
#         break
#     try:
#         answer = int(first_num)/ int(second_num)
#     except ZeroDivisionError:
#         print('math does not work like that')
#     else:
#         print(answer)

# filename = 'alice.txt'

# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     print(f'Sorry, the file {filename} is does not exist')


# #analyzing strings
# filename = 'practicefile-.txt'

# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     print(f'Sorry, the file {filename} is does not exist')
# else:
#     words = contents.split()
#     num_words = len(words)
#     print(f'The file {filename} has {num_words} words.')

# def count_words(filename):
#     """count aprox number of words"""
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         # print(f'Sorry, {filename} does not exist')
#         pass #choose to do nothing here
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f'The file {filename} has {num_words} words!')

# filenames = ['practicefile.txt', 'practice2.txt', 'xd.txt']

# for filename in filenames:
#     count_words(filename)
    
#storing data
# import json

# # numbers = [2,3,5,7,11,113]

# # filename = 'numbers.json'
# # with open(filename, 'w') as f_obj:
# #     json.dump(numbers, f_obj)

# filename = 'numbers.json'
# with open(filename) as f_obj:
#     numbers = json.load(f_obj)

# print(numbers)

#saving and reading user generated data (243)
# import json 
# username = input('What is your name? ')

# filename = 'username.json'
# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print(f"we'll remember you when u come back, {username}")

# with open(filename) as f:
#     username = json.load(f)
#     print(f'welcome back {username}!')

import json
def greet_user():
    username = get_stored_name()
    if username:
        print(f'Welcome back {username}!')
    else:
         username = get_new_username()
         print(f"we will remember u when u come back {username}!")
         
def get_stored_name():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
        username = input('what is ur name? ')
        filename = ('username.json')
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
        return username

greet_user()

