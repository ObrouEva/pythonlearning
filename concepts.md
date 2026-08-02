# Concepts I Master

## Template
- Concept :
- Definition :
- Example :

## Level 1 Concepts

import / modules
Definition : a module is a built-in toolbox you load with import. Gives access to ready-made functions and constants.
Example : import random → random.choice(list) picks one random element

functions — def / return / parameters
Definition : a function is a reusable block of code. Parameters let you pass different values each time you call it.
Example : def build_password(length, characters): → return password

while True / break — input validation
Definition : loops forever until a break is hit. Used to force valid user input.
Example : while True: if input.isdigit() and 6 <= n <= 50: break

any() — string inspection
Definition : returns True if at least one item in a sequence matches a condition.
Example : any(char.isdigit() for char in password)

try/except
Definition : attempts code that might crash, catches the error instead of crashing
Example : try: int(input()) / except ValueError: print("Numbers only")

dictionary
Definition : one variable that holds multiple key/value pairs
Example : config = {'length': 12, 'digits': True} → access with config['length']

DRY — Don't Repeat Yourself
Definition : if you write the same logic twice, turn it into a reusable function
Example : ask_yes_no(question) called twice instead of two identical while True loops

''.join()
Definition : joins a list of characters into a single string with nothing between them
Example : ''.join(['a', 'b', 'c']) → 'abc'

random.choices(pool, k=n)
Definition : picks n items at once from a pool, returns a list
Example : random.choices(string.ascii_letters, k=8) → 8 random letters
random.shuffle(list)
Definition : randomizes the order of a list in place
Example : random.shuffle(['a', '1', '!']) → ['!', 'a', '1']

with open() as f
Definition : opens a file safely, closes it automatically when done
Example : with open('passwords.txt', 'w') as f: f.write
("hello\n")

_ in for loops
Definition : used instead of i when the loop variable is not needed
Example : for _ in range(10): means "repeat 10 times, I don't need the counter"

list.append()
Definition : adds one item to the end of a list
Example : guaranteed = [] → guaranteed.append('7') → ['7']

dictionary — counting pattern
Definition : use a dict to count occurrences — check if key exists, add 1 or start at 1
Example : if word in counts: counts[word] += 1 else: counts[word] = 1

sorted() with lambda
Definition : sorts a list by a specific element using a mini anonymous function
Example : sorted(counts.items(), key=lambda x: x[1], reverse=True) sorts by count highest first

str.strip()
Definition : removes specified characters from the edges of a string
Example : 'python,'.strip('.,!?') → 'python'

with open() — read mode
Definition : opens a file safely and closes it automatically even if something crashes
Example : with open('file.txt', 'r') as f: text = f.read()

enumerate() / manual counter
Definition : tracks position in a loop
Example : i = 1 / i += 1 inside loop to number items 1, 2, 3...