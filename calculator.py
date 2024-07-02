# Starting the first PYTHON PRACTICE PROJECT starring Cinthia Morais
# Today's project is a... CALCULATOR!

def number_input(prompt):
    while True:
        valor = input(prompt)
        try:
        #converter para float
            return float(valor)
        except ValueError:
        #se houver uma virgula substitui para ponto e tenta de novo
            if ',' in valor:
                try:
                    return float(valor.replace(',','.'))
                except ValueError:
                    print('Invalid Value. Try Again\n')
            else:
                print('Invalid Value. Try Again\n')
def operator_input():
    valid_operator = ['+', '-', '*', '/', '%']
    while True:  
        operation = input('\nEnter the calculation operator you would like to use: \n+ for addition, - for subtraction, * for multiplication, / for division, % for percentage: ')
        if operation in valid_operator:
            return operation
        else:
            print('You have not type a valid operator, please try again.\n')

        
print('+--------------------------+')
print('| Welcome to PyCalculator! |')
print('+--------------------------+\n')

def pycalculator():        
    
     
    nmb1 = number_input('Enter your first number: ')
    operation = operator_input()
    nmb2 = number_input('\nEnter your second number: ')

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
        if nmb2 != 0:
            print('{} / {} = {}'.format(nmb1, nmb2, nmb1 / nmb2))
        else:
            print("Não é possivel dividir por zero")

    # Percentage
    elif operation == '%':
        print('{} % {} = {}'.format(nmb1, nmb2, nmb1 * (nmb2 / 100)))
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
\n''')
    if calc_again.upper() == 'Y':
        pycalculator()
    elif calc_again.upper() == 'N':
        print('\nSee you later. Bye!')
    else:
        again()

pycalculator()
