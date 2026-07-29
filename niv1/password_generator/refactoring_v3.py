import random 
import string 
 
def ask_yes_no(question):
    while True:
        answer = input(question).lower()
        if answer in ('y', 'n'):
            return answer 
        print('Please enter y or n.')

def get_length():
    while True:
        try: 
            n = int(input('Length (6-50): '))
            if 6 <= n <= 50:
                return n 
            print('Out of range')
        except ValueError:
           print('Not a number.')

def build_password(length, use_digits, use_special):
    pool = string.ascii_letters
    if use_digits == 'y':
        pool += string.digits
    if use_special == 'y':
        pool += string.punctuatoon
    return ''.join(random.choice(pool) for _ in range(length))

def main():
    use_digits = ask_yes_no('Include numbers? (y/n):')
    use_special = ask_yes_no('Include specials? (y/n): ')
    length = get_length()
    password = build_password(length, use_digits, use_special)
    print(f'Password: {password}')

main()

# If you write the same logic twice, turn it into a function.