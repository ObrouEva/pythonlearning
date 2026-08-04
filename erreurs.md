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

Bug — Text Analyzer Step 4
Bug : FileNotFoundError: No such file or directory: 'sample.txt'
Cause : Python looks for the file relative to where the script is run from, not where the script lives
Fix : use full relative path 'niv1/text_analyser/sample.txt' or cd into the correct folder before running

Bug — Text Analyzer Step 5
Bug : python, and python counted as different words
Cause : .split() doesn't remove punctuation — comma stays attached to word
Fix : word.strip('.,!?;:') before counting

Bug — Text Analyzer Mini Exam
Bug : for line in f after f.read() returned nothing
Cause : f.read() moves cursor to end of file — nothing left to read
Fix : use text.split('\n') to get lines from the string, loop over that instead

Bug — Text Analyzer Mini Exam
Bug : dates like 2024-01-15 appearing in top words
Cause : len(word) > 2 filter doesn't exclude numbers
Fix : add and not word[0].isdigit() to skip words starting with a digit

Bug — Log Parser Step 4
Bug : counts = {} inside the loop reset dictionary every iteration
Cause : wrong indentation — dictionary must be defined before the loop
Fix : move counts = {} outside the loop

Bug — Log Parser Step 4
Bug : ip (match object) used as dictionary key instead of ip_str (string)
Cause : forgot to call .group() to extract the string from the match object
Fix : always extract with ip_str = ip.group() then use ip_str as key

Bug — Log Parser Step 5
Bug : error lines section only checked last line instead of all lines
Cause : second loop missing — only checked ip, date, status from last iteration
Fix : add a second for line in lines loop for the error lines section

Bug — Log Parser Mini Exam
Bug : error counting block outside if ip and date and status check
Cause : wrong indentation — status.group(1) called on potential None
Fix : move error counting inside the if ip and date and status block