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
