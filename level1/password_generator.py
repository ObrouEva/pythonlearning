import random
import string

def ask_length():
    while True:
     try: 
        length = int(input('How long should the password be? '))
        if 8 <= length <= 64:
           return length
        else:
           print('Please type an number between 8 and 64!')
     except ValueError:
         print('Type a number!')

def ask_yes_no(question):
    while True:
        answer = input(question)
        if answer == 'y' or answer == 'n':
            return answer
        else: 
            print('Please type y or n')

def build_password(length,numbers,special):
    pool = string.ascii_letters
    password = ""
    if 'y' in numbers:
          pool += string.digits
    if 'y' in special:
          pool += string.punctuation
    for i in range(length):
       password += random.choice(pool)
    return password

def calucate_score(password):
    points = 0 

    if len(password) >= 8:
        points += 20
    if len(password) >= 12: 
        points += 20
   
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for element in password:
        if element.islower():
            has_lower = True
        if element.isupper():
            has_upper = True
        if element.isdigit():
            has_digit = True
        if element in string.punctuation:
            has_special = True
    
    if has_lower:
        points += 20
    if has_upper:
        points += 20
    if has_digit:
        points += 20
    if has_special:
        points += 20

    return points

#main block
length = ask_length()
numbers = ask_yes_no('Include numbers (y/n)? ')
special = ask_yes_no('Include special characters (y/n)? ')
password = build_password(length,numbers,special)
print(password)

if numbers == 'n' and special == 'n':
    print('Password Strength: WEAK')
elif numbers == 'n' or special == 'n':
    print('Password Strenth:  MEDIUM')
else:
    print('Password strength: STRONG')

print(calucate_score(password))

with open('passwords.txt', 'w') as f:
    for i in range(10):
        password = build_password(length, numbers, special)
        f.write(password + '\n')

print('10 password saved to password.txt')