import random 
import string 

def get_length():
  while True:
    try:
      length = int(input('Password length: '))
      if 6 <= length <= 50:
        return length
      print('Must be between 6 and 50.')
    except ValueError:
      print('Numbers only.')
# try/except says: "attempt this -if it explodes, handle it here instead of crashing."

def get_characters():
  pool = string.ascii_letters
  if input('Numbers? (y/n): ').lower() == 'y':
    pool += string.digits
  if input('Specials? (y/n): ').lower() == 'y':
    pool += string.punctuation
  return pool
# Just ask, check, build pool, return it. Minimal 

def build_password(length, pool):
  return ''.join(random.choice(pool) for _ in range(length))

def main():
  pool = get_characters()
  length = get_length()
  password = build_password(length, pool)
  print(f'Password: {password}')

main()