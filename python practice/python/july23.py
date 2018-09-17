import unittest
def get_formatted_name(first, last, middle=''):
    """generate a full name"""
    if middle:
        full_name = first.rstrip() + ' ' + middle.rstrip() + ' ' + last.rstrip()
    else:
        full_name = first.rstrip() + ' ' + last.rstrip()
    return full_name.title()

print('Enter q any time to quit. ')
while True:
    first = input('\nPlease give a first name: ')
    if first == 'q':
        break
    last = input('Please give a last name: ')
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print(f'Formatted name: {formatted_name}.')

#continute on testing classes

