import random
import string


while True:
     try: 
        length = int(input('How long should the password be? '))
        if 8 <= length <= 64:
           break
        else:
           print('Please type an number between 8 and 64!')
     except ValueError:
         print('Type a number!')

while True:
    numbers = input('Include numbers (y/n)? ')
    if numbers == 'y' or numbers == 'n':
        break
    else:
        print('Please type y or n')

while True:
    special_characters = input('Include special characters (y/n)? ')
    if special_characters == 'y' or special_characters == 'n':
        break
    else:
        print('Please type y or n')



def build_password(length,numbers,special_characters):
    pool = string.ascii_letters
    password = ""
    if 'y' in numbers:
          pool += string.digits
    if 'y' in special_characters:
          pool += string.punctuation
    for i in range(length):
       password += random.choice(pool)
    return password

password = build_password(length,numbers,special_characters)
print(password)

if numbers == 'n' and special_characters == 'n':
    print('Password Strength: WEAK')
elif numbers == 'n' or special_characters == 'n':
    print('Password Strenth:  MEDIUM')
else:
    print('Password strength: STRONG')

def calucate_score(password):
    points = 0 
    special=('!','@','#','$','%','^','&','*','(',')','-','_','+','=','')

    if len(password) >= 8:
        points += 20
    elif len(password) >= 12: 
        points += 20

    for element in password:
        if element.islower:
            points += 20
        if element.isdigits:
            points += 20

    if element in string.punct:
        points += 20

    return points

print(calucate_score(password))
#4 spaces indetations