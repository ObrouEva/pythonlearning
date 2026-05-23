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

PROGRESSION.MD — ADD THIS :

 Password Generator — 70% mastery — Steps 1-4 complete, mini challenge done, score function has bugs being fixed


ERREURS.MD — ADD THIS :
Bug — Password Generator Step 4

Bug : elif used instead of second if for length check
Cause : elif only runs if the first if is False, so >= 12 was never reached
Fix : use two separate if statements so both length bonuses can trigger

Bug — Password Generator Step 4

Bug : element.islower and element.isdigits written without parentheses
Cause : without () Python references the method but never calls it — always evaluates as True
Fix : element.islower() and element.isdigit() with parentheses, and correct name isdigit not isdigits

Bug — Password Generator Step 4

Bug : score adds 20 points for every character that matches, not once
Cause : points += 20 inside the loop triggers on each matching character
Fix : use a bool flag outside the loop, set it to True when found, add points after the loop

Bug — Password Generator Step 4

Bug : special character check if element in special placed outside the for loop
Cause : indentation error — only checks the last character of the password
Fix : move inside the loop, or use a bool flag pattern with string.punctuation