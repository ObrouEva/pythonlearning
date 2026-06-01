# Concepts I Master

## Template
- Concept :
- Definition :
- Example :

## Level 1 Concepts

import / modules

Definition : import module_name loads a Python built-in toolbox. Access its tools with module_name.tool
Example : import random then random.choice(my_list) picks one random element

string module constants

Definition : string.ascii_letters, string.digits, string.punctuation are ready-made character strings
Example : pool = string.ascii_letters + string.digits gives all letters and numbers

bool conversion from input

Definition : convert a string answer to bool using == and store it with =
Example : use_digits = input("y/n? ") == "y" stores True if user typed y, else False

functions — def / return / parameters

Definition : def name(param): defines a reusable block. return sends a value back. Parameters are local to the function.
Example : def build_password(length): ... return password

+= shorthand

Definition : x += y is identical to x = x + y, used to accumulate values
Example : password += random.choice(pool) adds one character each iteration

while True / break

Definition : while True loops forever until a break statement is hit — used to keep asking for input until valid
Example : while True: x = input("y/n? ") \ if x == "y" or x == "n": break

try / except

Definition : try attempts a risky block, except ErrorType catches the crash and runs a fallback instead
Example : try: x = int(input("number? ")) \ except ValueError: print("not a number")

string methods — isupper / islower / isdigit

Definition : called on a single character with (), returns True or False — must include parentheses to actually call the method
Example : "A".isupper() returns True, "1".isdigit() returns True

bool flag pattern

Definition : set a variable to False before a loop, set it to True inside when condition is met, check it after the loop to add points or trigger logic once
Example : has_digit = False \ for char in password: \ if char.isdigit(): has_digit = True \ if has_digit: score += 20

len()

Definition : returns the number of characters in a string or items in a list
Example : len("hello") returns 5

file writing — open / write / with

Definition : open('file.txt', 'w') creates or overwrites a file. f.write(text) writes a string. with closes the file automatically when done
Example : with open('passwords.txt', 'w') as f: f.write(password + '\n')

function structure — define first, call after

Definition : all functions must be defined before the main block runs. Python reads top to bottom — calling a function before defining it causes a NameError
Example : define ask_length(), build_password(), calculate_score() first, then call them in the main block at the bottom

return vs break

Definition : break exits a loop. return exits a function AND sends a value back to the caller
Example : inside ask_length(), use return length instead of break so the value is passed back

ictionary — key/value pairs

Definition : {} stores data as key:value pairs. Access by key, not by position. Keys must be unique.
Example : word_count["python"] = 4 — key is "python", value is 4

dictionary — if/else counting pattern

Definition : check if key exists first, add 1 if yes, create at 1 if no
Example : if word in word_count: word_count[word] += 1 else: word_count[word] = 1

.items() and tuple unpacking

Definition : .items() returns each key-value pair as a tuple. Two variables unpack both at once.
Example : for word, count in word_count.items(): print(word, count)

f-strings

Definition : f"" strings let you embed any variable directly inside a string — Python converts automatically
Example : f"{word} : {count}" — no need for str() or +

sorted() with lambda

Definition : sorted(list, key=lambda x: x[1], reverse=True) sorts by the second element of each pair, highest first
Example : sorted(word_count.items(), key=lambda x: x[1], reverse=True) sorts words by frequency

list slicing

Definition : [:n] takes only the first n items from a list
Example : sorted_words[:3] returns only the top 3 words

file reading — open / read / with

Definition : open('file.txt', 'r') opens existing file for reading. f.read() returns full content as string. 'r' = read, 'w' = write/create, 'a' = append
Example : with open('sample.txt', 'r') as f: text = f.read()

set() for unique values

Definition : set() removes all duplicates automatically. len(set(words)) counts unique items
Example : len(set(['python', 'is', 'python'])) returns 2

list slicing with [-1]

Definition : negative index accesses items from the end of a list. [-1] = last item
Example : line.split()[-1] gets the last word of a line — useful for status codes in logs

enumerate() with start value

Definition : enumerate(list, 1) gives index + value pairs, starting count at 1 instead of 0
Example : for i, (word, count) in enumerate(sorted_words[:5], 1): print(f'{i}. {word}')

extracting fields from structured text

Definition : log files are space-separated. line.split()[0] gets first field (IP), line.split()[-1] gets last field (status code)
Example : ip = line.split()[0] extracts IP from '192.168.1.1 - - [date] "GET /" 200'

continue — skip current loop iteration

Definition : continue skips the rest of the current loop iteration and moves to the next one
Example : if line == '': continue skips empty lines without crashing

log parsing — extracting fields

Definition : log lines are space-separated. Use split()[0] for first field, split()[-1] for last field
Example : ip = line.split()[0] → '192.168.1.1', status = line.split()[-1] → '200'

counting inside a loop vs len()

Definition : when you need to count only valid items, increment a counter inside the loop instead of using len() on the whole list
Example : total = 0 then total += 1 inside loop after empty line check

re.search() vs re.findall()

Definition : re.findall() returns all matches as a list. re.search() returns the first match as a match object or None
Example : re.findall(r'\d+', text) → ['192', '168'] / re.search(r'\d+', text).group() → '192'

match object and .group()

Definition : re.search() returns a match object, not a string. .group() extracts the actual matched text
Example : match = re.search(r'\d+\.\d+\.\d+\.\d+', line) then match.group() → '192.168.1.1'

regex OR operator

Definition : | means OR in regex — matches either pattern
Example : re.search(r'404|403', line) matches lines containing 404 or 403

regex special characters

Definition : \d = one digit, \d+ = one or more digits, \. = literal dot, | = or, r'' = raw string
Example : r'\d+\.\d+\.\d+\.\d+' matches any IP address pattern