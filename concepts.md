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

