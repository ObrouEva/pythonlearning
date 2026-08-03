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

password = build_password(number, characters)
print(f'Your password is: {password}')

def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if  len(password) >= 12:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1
    
    if score <= 1:
        return 'Strength: Weak'
    elif 2 <= score < 4:
        return 'Strength: Medium'
    else:
        return 'Strength : Strong'

print(password_strength(password))
