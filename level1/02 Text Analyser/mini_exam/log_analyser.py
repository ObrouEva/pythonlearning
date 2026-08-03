with open('niv1/text_analyser/mini_exam/system.log', 'r') as f: 
    text = f.read()

error = 0
warning = 0
info = 0
    
words = text.lower().split()
lines = text.split('\n')

for line in lines:
    if 'ERROR' in line:
        error += 1
    if 'WARNING' in line:
        warning += 1
    if 'INFO' in line:
        info += 1  

counts = {}
for word in words:
    word = word.strip('.,!?;:') # remove punctuation from edges
    if len(word) > 2 and not word[0].isdigit(): # ← only count words longer than 2 chars
        if word in counts:
            counts[word] += 1 
        else:
            counts[word] = 1 

sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)
     

print(f'===== Text Report =====')
print(f'Total lines   : {len(lines)}')
print(f'ERROR count   : {error}')
print(f'WARNING count : {warning}')
print(f'INFO count    : {info}\n')
print('Top 3 most frequent words:')
i = 1
for word, count in sorted_words[:3]:
    print(f'{i}. {word}: {count}')
    i += 1
print(f'=======================')