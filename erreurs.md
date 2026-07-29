# My Classic Errors

## Template
- Bug :
- Cause :
- Fix :

## Errors Log
### Bug — Password Generator

Bug : digits.lower instead of digits.lower()
Cause : referenced the method without calling it, missing ()
Fix : always add () to call a method

Bug : if digits.lower == 'y' inside the special block
Cause : copy-paste error, checking wrong variable
Fix : match the variable to the block you're in (special == 'y')

Bug : if 2 < score < 4 for Medium strength
Cause : strict inequality excluded score == 2
Fix : use 2 <= score < 4

Bug : build_password(length, characters) passing string instead of int
Cause : length was raw input string, validated int was stored in number
Fix : pass number to the function, not length

Bug : characters defined outside get_characters() then modified inside
Cause : can't modify an outside variable from inside a function like this
Fix : define characters = string.ascii_letters inside the function

Bug : return number inside the while True loop in get_length()
Cause : wrong indentation — return ran on first iteration before validation completed
Fix : dedent return number to be outside the loop, same level as while True

Bug : password and strength generated outside the loop
Cause : both variables defined before for i in range() so same password written 10 times
Fix : move both inside the loop so a new password is generated each iteration

Bug : range(1, 10) only generates 9 passwords
Cause : range(1, 10) = 1 to 9 inclusive
Fix : use range(1, 11) to get 1 to 10

Bug : print() had wrong indentation inside with block
Cause : print was inside the with block instead of after it
Fix : dedent print to same level as with open(...)