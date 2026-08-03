import random
import string

characters = string.ascii_letters 

digits = input('Include numbers? (y/n) ')
if digits.lower() == 'y':
    characters += string.digits

special = input('Include special characters? (y/n) ')
if special.lower() == 'y':
    characters += string.punctuation

while True: 
    length = input('How long should the password be? ')
    if length.isdigit():
        number = int(length)
        if 6 <= number <= 50:
            break
        else:
            print('Must be between 6 and 50!')
    else:
        print('Please enter a number!')

def build_password(number, characters):       #recieve as parameter
    password = ''
    for i in range(number):
        password += random.choice(characters)
    return password       



print(f'Your password is: {build_password(number, characters)}')
