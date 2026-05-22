import random 
import string

numbers = input('Include numbers (yes/no)? ')
special_characters = input('Include special characters (yes/no)? ')

def build_password(numbers, special_characters):
    pool = string.ascii_letters
    if numbers == 'yes':
        pool += string.digits
    if special_characters == 'yes':
        pool += string.punctuation
    return pool

pool = build_password(numbers, special_characters)
print(pool)