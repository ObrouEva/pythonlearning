import random
import string

def build_password(length, use_digits, use_special):
    pool = string.ascii_letters
    guaranteed = [] # start with empty list

    if use_digits: 
        pool += string.digits 
        guaranteed.append(random.choice(string.digits)) # force at least one digit
    if use_special: 
        pool += string.punctuation
        guaranteed.append(random.choice(string.punctuation)) # force at least one special

    remaining = length - len(guaranteed) 
    # if length=10 and guarenteed has 2 items → remaining = 8
    password_list = guaranteed + random.choices(pool, k= remaining)
    # glue guaranteed chars + 8 random chars into one list
    random.shuffle(password_list) #randomized order
    return ''.join(password_list)

# force at least one digit and one special → fihure out how many randoms chard are still needed → fill the test v shuffle everything → return as string

def main():
    use_digits = input('Numbers? (y/n): ').lower() == 'y'
    use_speical = input('Specials? (y/n); ').lower() =='y'
    length = int(input('Length: '))
    print(build_password(length, use_digits, use_speical))

main()
