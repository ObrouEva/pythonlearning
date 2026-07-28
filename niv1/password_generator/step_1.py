import random
import string

characters = string.ascii_letters + string.digits

length = int(input('How long should the password be? '))

def build_password():       
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password       



print(f'Your password is: {build_password()}')
