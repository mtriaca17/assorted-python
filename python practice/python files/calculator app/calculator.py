#Calculator app
def add_nums(num1, num2):
    ans = num1 + num2
    return ans

def sub_nums(num1, num2):
    diff = num1 - num2
    return diff

def multiply_nums(num1, num2):
    product = num1 * num2
    return product

def divide_nums(num1, num2):
    try:
       ans = num1/num2
       return ans
    except ZeroDivisionError:
        ans = 'You tried to divide by zero, you cant do that!'
        return ans

def repeat():
    ask_repeat = input(''' 
do you want to calculate again? Y for yes N for no.
    ''')

    if ask_repeat.upper() == 'Y':
        main()
    elif ask_repeat.upper() == 'N':
        print('Bye bye')
    else:
        repeat()


def main():
    operation = ''
    while operation not in ('add', 'sub', 'multiply', 'divide'):
        operation = input('What operation?(add, sub, multiply, divide): ').rstrip()
        
    num1 = int(input('First number: '))
    num2 = int(input('Second number: '))

    if operation == 'add':
        ans = (add_nums(num1, num2))
    elif operation == 'sub':
        ans = (sub_nums(num1, num2))
    elif operation == 'multiply':
        ans = (multiply_nums(num1, num2))
    elif operation == 'divide':
        ans = (divide_nums(num1, num2))
    
    print(f'\nthe answer for operation {operation} is {ans}\n')

print('Welcome to the Calculator!')
main()
repeat()

