# Starting the first PYTHON PRACTICE PROJECT starring Cinthia Morais
# Today's project is a... CALCULATOR!

# To begin with, we will ask the user to enter the numbers they will calculate, 
# for this we will use some variales, the input function and we are gonna to convert the 
# insert numbers from string to float

input('To get started, please press enter.')

nmb1 = float(input('Enter your first number: '))
nmb2 = float(input('Enter your second number: '))

# Addition
print('{} + {} = {}'.format(nmb1, nmb2, nmb1 + nmb2))

# Subtraction
print('{} - {} = {}'.format(nmb1, nmb2, nmb1 - nmb2))

# Multiplication
print('{} x {} = {}'.format(nmb1, nmb2, nmb1 * nmb2))

# Division
print('{} / {} = {}'.format(nmb1, nmb2, nmb1 / nmb2))