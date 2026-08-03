import random
import string

def get_config(): #stores all user choices in one dictionary
    return {
      'length': int(input('Length: ')), 
      # Step 1 : asks "Length: " → user types 12 → stores 12
      'digits': input('Numbers? (y/n): ').lower() == 'y', 
      # Step 2 : asks "Numbers?" → user types 'y' → 'y' == 'y' → True
      'special': input('Specials? (y/n): ').lower() == 'y' 
      # Step 3 : asks "Specials?" → user types 'n' → 'n' == 'y' → False

    }

def build_pool(config):
    pool = string.ascii_letters
    if config['digits']: # same as : if True
        pool += string.digits
    if config['special']: # same as : if False → skip
        pool += string.punctuation
    return pool

def build_password(config):
    pool = build_pool(config) #→ calls build_pool(config) to get the character pool
    return ''.join(random.choice(pool) for _ in range(config['length'])) 
#  → generates password using config['length']
#  → returns password

def main():
    config = get_config()  # ask everything → one object
    password = build_password(config) # pass one object
    print(f'Password: {password}') #prints it

main()