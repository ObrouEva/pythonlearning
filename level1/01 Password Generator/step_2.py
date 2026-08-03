import random
import string

characters = string.ascii_letters 

digits = input('Include numbers? (y/n) ')
if digits.lower() == 'y':
    characters += string.digits

special = input('Include special characters? (y/n) ')
if special.lower() == 'y':
    characters += string.punctuation

length = int(input('How long should the password be? '))

def build_password(length, characters):       #recieve as parameter
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password       



print(f'Your password is: {build_password(length, characters)}')
