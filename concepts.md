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