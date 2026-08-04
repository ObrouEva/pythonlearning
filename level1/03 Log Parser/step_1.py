import re # → python module for pattern matching inside strings 
#you already know 'ERROR' in line ) that checks if an exact word exits. But what if you don't know the exact word? What if you just know the shap of what you're looking for? 

with open('level1/03 Log Parser/access.log', 'r') as f: 
    text = f.read()

lines = text.split('\n')
for line in lines:
    ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line) # look for the pattern inside the string and the string to search inside
    # \d means 'any single digit'
    # \d+ means 'one or more digits'
    # \. means a literal dot '.'
    if ip_match:
        print(f'Found IP: {ip_match.group()}') # → match.group() gives you the actual text that matched.s