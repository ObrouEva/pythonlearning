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

for line in f vs f.read()
Definition : f.read() loads entire file as one string; for line in f reads one line at a time — can't combine both on same file handle
Example : text = f.read() then for line in text.split('\n'): to loop over lines

'substring' in string
Definition : checks if a string contains another string, returns True or False
Example : 'ERROR' in line → True if the word ERROR appears anywhere in that line

word[0].isdigit()
Definition : checks if the first character of a string is a digit
Example : '2024-01-15'[0].isdigit() → True — used to filter out dates and numbers

import re — regex basics
Definition : module for pattern matching inside strings when you don't know the exact value
Example : re.search(r'\d+\.\d+\.\d+\.\d+', line) finds an IP address

regex patterns
Definition : \d = any digit, \d+ = one or more digits, \. = literal dot, \d{3} = exactly 3 digits
Example : r'\d+\.\d+\.\d+\.\d+' matches any IP like 192.168.1.

re.search() + .group()
Definition : finds first match of pattern in string, .group() extracts the matched text, .group(1) extracts first capture group
Example : match = re.search(r'\d{3}', line) then match.group() → '404'

capture groups ()
Definition : parentheses in a regex pattern create a group you can extract separately with .group(1)
Example : re.search(r'\[(\d+/\w+/\d+)\]', line).group(1) extracts date without brackets

dict.get(key, default)
Definition : safely retrieves a value from a dict, returns default if key doesn't exist instead of crashing
Example : error_counts.get(ip_str, 0) returns 0 if IP has no errors

list.append(item)
Definition : adds one item to the end of a list
Example : tasks.append('Buy groceries') → adds task to list

list.pop(index)
Definition : removes and returns item at given index
Example : tasks.pop(0) removes first item, tasks.pop(number - 1) for 1-based user input

enumerate(list, start)
Definition : loops over a list giving both index and value, start sets the starting number
Example : for i, task in enumerate(tasks, 1): → numbered list starting at 1

if not list
Definition : checks if a list is empty — returns True if empty
Example : if not tasks: print('No tasks.')

json.dump() / json.load()
Definition : saves Python object to JSON file / loads JSON file back into Python object
Example : json.dump(tasks, f) saves list, json.load(f) loads it back