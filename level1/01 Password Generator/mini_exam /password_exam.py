import random
import string

def get_config(): 
    return {
      'length': int(input('Length: ')), 
      'digits': input('Numbers? (y/n): ').lower() == 'y', 
      'special': input('Specials? (y/n): ').lower() == 'y' 
    }

def build_pool(config):
    pool = string.ascii_letters
    if config['digits']: 
        pool += string.digits
    if config['special']:
        pool += string.punctuation
    return pool

def build_password(config):
    pool = build_pool(config) 
    return ''.join(random.choice(pool) for _ in range(config['length'])) 

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
    config = get_config()       

    with open('passwords.txt', 'w') as f:
        for i in range(1,11):
            password = build_password(config)
            strength = password_strength(password)
            f.write(f"Password {i}: {password} - {strength}\n")
    print("Saved 10 passwords to passwords.txt")

main()