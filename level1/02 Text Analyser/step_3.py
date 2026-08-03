
text = """Python is amazing. Do you agree?
I think it is great! Let's keep learning.
Cybersecurity is important. Stay safe online!"""

words = text.lower().split()
lines = text.split('\n')
sentences = 0
for char in text:
    if char in '.?!':
        sentences += 1

print(f'===== Text Report =====')
print(f'Words      : {len(words)}')
print(f'Lines      : {len(lines)}')
print(f'Characters : {len(text)}')
print(f'Sentences  : {sentences}')
print(f'=======================')