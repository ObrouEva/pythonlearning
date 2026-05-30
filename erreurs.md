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

Bug — Password Generator Step 5

Bug : length = '' inside build_password overwrote the parameter
Cause : confused parameter with local variable initialization
Fix : remove the line — length already comes in as a parameter, no need to declare it

Bug — Password Generator Step 5

Bug : main block code scattered between function definitions
Cause : calling functions like length = ask_length() before all functions were defined
Fix : define all functions first, then run main block at the very bottom

Bug — Password Generator Step 6

Bug : flags has_lower, has_upper etc initialized inside the loop instead of before it
Cause : misplaced indentation — flags were reset on every iteration
Fix : initialize all flags to False before the for loop, set to True inside

Bug — Text Analyzer Step 2

Bug : numbered output not printed (1. 2. 3.)
Cause : missed detail in the exercise requirements
Fix : use enumerate() or a counter variable to add numbers before each line

Bug — Text Analyzer Step 4

Bug : opened sample.txt with 'w' mode instead of 'r'
Cause : confused read and write modes — 'w' overwrites the file
Fix : use 'r' to read existing files, 'w' only when creating output files

Bug — Text Analyzer Step 4

Bug : FileNotFoundError when opening sample.txt
Cause : file was not in the same folder as the script
Fix : either use full path or make sure file is in same directory as script

Bug — Text Analyzer Step 5

Bug : wrote report to sample.txt instead of report.txt
Cause : used same filename for both input and output — 'w' mode destroyed original data
Fix : always use a separate filename for output files

Bug — Text Analyzer Step 6

Bug : IP extracted with line[i][0:12] — character slice instead of split
Cause : hardcoded slice breaks for IPs of different lengths
Fix : use line.split()[0] to always get the first word regardless of length

Bug — Text Analyzer Step 6

Bug : looping over full lines but treating them as IPs in dictionary
Cause : variable naming confusion — ip was actually a full log line
Fix : extract IP first with line.split()[0], then use that in the dictionary

Bug — Text Analyzer Step 6

Bug : lines.split()[0] instead of line.split()[0] inside loop
Cause : confusion between lines (the full list) and line (one item from the loop)
Fix : inside a for line in lines loop, always use line for the current item

Bug — Text Analyzer Step 6

Bug : IndexError: list index out of range on line.split()[0]
Cause : empty string '' at end of file after split('\n') — .split()[0] crashes on empty string
Fix : add if line == '': continue at top of loop to skip empty lines

Bug — Text Analyzer Step 6

Bug : status code check used int comparison == 404 instead of string == '404'
Cause : line.split()[-1] returns a string, not an integer
Fix : always use quotes when comparing to values extracted from text

Bug — Text Analyzer Step 6

Bug : total_request = len(lines) counted the empty line
Cause : empty line created by split('\n') was included in the count
Fix : initialize total_request = 0 and increment inside the loop after the empty line check