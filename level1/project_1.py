import random
import string
pool = string.ascii_letters

length = int(input('How long should the password be? '))
numbers = input('Include numbers (y/n)? ')
special_characters = input('Include special characters (y/n)? ')
'y' == True
'n' == False

def build_password(length,numbers,special_characters):
    password = ""
    if 'y' in numbers:
          password += string.digits
    if 'y' in special_characters:
          password += string.punctuation
    for i in range(length):
       password += random.choice(pool)
    return password

print(build_password(length,numbers=True,special_characters=True))

#4 spaces indetations

