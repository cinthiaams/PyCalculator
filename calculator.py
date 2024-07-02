# Starting the first PYTHON PRACTICE PROJECT starring Cinthia Morais
# Today's project is a... CALCULATOR!

# To begin with, we will ask the user to enter the numbers they will calculate, 
# for this we will use some variales, the input function and we are gonna to convert the 
# insert numbers from string to float

valid_operator = ['+', '-', '*', '/', '%']
operation = input('''To get started: 
please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
% for percentage
''')
# in case of erro
if operation not in valid_operator:
    print('You have not type a valid operator, please run the program again.')
else:   
    nmb1 = float(input('Enter your first number: '))
    nmb2 = float(input('Enter your second number: '))

    # Addition
    if operation == '+':
        print('{} + {} = {}'.format(nmb1, nmb2, nmb1 + nmb2))

    # Subtraction
    elif operation == '-':
        print('{} - {} = {}'.format(nmb1, nmb2, nmb1 - nmb2))

    # Multiplication
    elif operation == '*':
        print('{} x {} = {}'.format(nmb1, nmb2, nmb1 * nmb2))

    # Division
    elif operation == '/':
        print('{} / {} = {}'.format(nmb1, nmb2, nmb1 / nmb2))

    # Percentage
    elif operation == '%':
        print('{} % {} = {}'.format(nmb1, nmb2, nmb1 * (nmb2 / 100)))