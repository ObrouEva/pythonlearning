# My Classic Errors

## Template
- Bug :
- Cause :
- Fix :

## Errors Log
Bug — Password Generator Step 1

Bug : return placed inside the for loop
Cause : indentation error, return was at loop level instead of function level
Fix : dedent return by one level so it runs after the loop completes

Bug — Password Generator Step 2

Bug : 'y' == True and 'n' == False written as standalone expressions
Cause : confusion between comparison and assignment — == evaluates, = assigns
Fix : use_digits = answer == "y" to store the bool result in a variable

Bug — Password Generator Step 2

Bug : pool built outside function and never updated based on user choices
Cause : digits and punctuation added to password directly instead of to pool before the loop
Fix : build pool dynamically inside the function before the for loop, then use it in random.choice(pool)

Bug — Password Generator Step 2

Bug : function called with hardcoded numbers=True, special_characters=True
Cause : user input variables not passed to the function call
Fix : call with actual variables build_password(length, numbers, special_characters)