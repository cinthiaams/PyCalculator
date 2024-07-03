'''Starting the first PYTHON PRACTICE PROJECT starring Cinthia Morais
Today's project is a... CALCULATOR!'''

def number_input(prompt):
    '''takes the input and converts to float'''
    while True:
        valor = input(prompt)
        try:
        # Convert to float
            return float(valor)
        except ValueError:
        # If there is a comma, replace it with a period and try again
            if ',' in valor:
                try:
                    return float(valor.replace(',','.'))
                except ValueError:
                    print('Invalid Value. Try Again\n')
            else:
                print('Invalid Value. Try Again\n')
# Function for inputting operator
def operator_input():
    '''receive the input for operator'''
    valid_operator = ['+', '-', '*', '/', '%']
    while True:
        operation = input('''\nEnter the operator you would like to use:
+ for addition, - for subtraction, * for multiplication, 
/ for division, % for percentage: ''')
        if operation in valid_operator:
            return operation
        print('You have not type a valid operator, please try again.\n')

print('+--------------------------+')
print('| Welcome to PyCalculator! |')
print('+--------------------------+')

# PyCalculator main function
def pycalculator():
    '''calculator main function'''
    nmb1 = number_input('\nEnter your first number: ')
    operation = operator_input()
    nmb2 = number_input('\nEnter your second number: ')

    # Addition
    if operation == '+':
        print(f'\n{nmb1} + {nmb2} = {nmb1 + nmb2}')

    # Subtraction
    elif operation == '-':
        print(f'\n{nmb1} - {nmb2} = {nmb1 - nmb2}')

    # Multiplication
    elif operation == '*':
        print(f'\n{nmb1} x {nmb2} = {nmb1 * nmb2}')

    # Division
    elif operation == '/':
        if nmb2 != 0:
            print(f'\n{nmb1} / {nmb2} = {nmb1 / nmb2}')
        else:
            print("\nIt is not possible to divide by zero")

    # Percentage
    elif operation == '%':
        print(f'\n{nmb1} % {nmb2} = {nmb1 * (nmb2 / 100)}')
    again()
# Function to know if the user would like to calculate again
def again():
    '''
    Prompt the user if they want to perform another calculation.
    '''
    calc_again = input('''\nDo you want to calculate again?
Please type Y for YES or N for NO.\n''')
    if calc_again.upper() == 'Y':
        pycalculator()
    elif calc_again.upper() == 'N':
        print('\nSee you later. Bye!')
    else:
        again()

pycalculator()
