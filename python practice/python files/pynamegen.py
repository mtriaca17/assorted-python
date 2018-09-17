import string
import random

def generator():
	letter1 = random.choice(string.ascii_lowercase)
	letter2 = random.choice(string.ascii_lowercase)
	letter3 = random.choice(string.ascii_lowercase)
	letter4 = random.choice(string.ascii_lowercase)
	letter5 = random.choice(string.ascii_lowercase)
	name = letter1+letter2+letter3+letter4+letter5
	return name

print(generator())


vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letter = string.ascii_lowercase

if letter_input_1