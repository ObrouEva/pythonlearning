import random
import string

def get_characters():
  characters = string.ascii_letters
  while True: 
    digits = input('Include numbers? (y/n) ')
    if digits.lower() in ('y', 'n'):
        if digits.lower() == 'y':
            characters += string.digits
        break
    else:
        print('Please enter y or n')
  while True:
     special = input('Include special characters? (y/n) ')
     if special.lower() in ('y', 'n'):
        if special.lower() == 'y':
            characters += string.punctuation
        break
     else:
         print('Please enter y or n')   
  return characters

def get_length():
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
   return number
  
def build_password(number, characters):
    password = ''
    for i in range(number):
        password += random.choice(characters)
    return password  

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

def main():
    characters = get_characters()
    length = get_length()
    password = build_password(length, characters)
    print(f'Your password is: {password}')
    print(password_strength(password))

main()