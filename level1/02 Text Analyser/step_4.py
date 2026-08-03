with open('niv1/text_analyser/sample.txt', 'r') as f: #with open garantees the file gets closed when the block ends even if something creashed inside
    text = f.read()   #read only

words = text.lower().split()
lines = text.split('\n')
sentences = 0
for char in text:
    if char in '.?!':
        sentences += 1
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1 
    else:
        counts[word] = 1 
        
print(f'===== Text Report =====')
print(f'Words      : {len(words)}')
print(f'Lines      : {len(lines)}')
print(f'Characters : {len(text)}')
print(f'Sentences  : {sentences}')
print(f'=======================')