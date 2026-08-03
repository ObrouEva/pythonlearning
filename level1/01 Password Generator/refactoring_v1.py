import random 
import string

def get_length():
  while True: 
    try:
      length = int(input('Password length: '))
      if 6 <= length <= 50:
        return length 
      print('Must be between 6 and 50')
    except ValueError: 
      print('Numbers only.')
  
def get_characters():
  pool = string.ascii_letters
  if input('Numbers, (y/n): ').lower() == 'y':
    pool += string.digits

  if input('Specials? (y/n): ').lower() == 'y':
    pool += string.punctuation
  return pool


def build_password(length, pool):
  return ''.join(random.choice(pool) for _ in range(length)) #pick one random character from pool, repeat length times, glue them all together with nothing between them, return the result

# ''.join(...)
# join() glues a list of chracter together 
# '' means 'glue them with nothing between them'
# ['a','b','c'] → 'abc'

# for _in range(length)
# same as your for loop 
# _ is used instead for i when you don't use the loop variable
# it just means "repeat length times, i don't care about the number"

# random.choice(pool)
# picks on random chracter each time the loop runs

def main(): 
  pool = get_characters() #1. ask options, get back the character pool
  length = get_length() #2. ask length, get back a valid number
  password = build_password(length, pool) #3. generate password
  print(f'Password: {password}') #4. show it 

main() #5. actually run everything