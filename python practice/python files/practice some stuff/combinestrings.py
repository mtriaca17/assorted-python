string1 = 'ducky'
string2 = 'gibbs'

string_combine = ''
counter = 0

for letter in string2:
    string_combine += string2[counter]
    string_combine += string1[counter]
    counter+=1

print(string_combine)