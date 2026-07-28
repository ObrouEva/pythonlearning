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