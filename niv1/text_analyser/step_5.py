with open('niv1/text_analyser/sample.txt', 'r') as f: 
    text = f.read()   


words = text.lower().split()
lines = text.split('\n')
sentences = 0
for char in text:
    if char in '.?!':
        sentences += 1
counts = {}
for word in words:
    word = word.strip('.,!?;:') # remove punctuation from edges
    if len(word) > 2: # ← only count words longer than 2 chars
      if word in counts:
          counts[word] += 1 
      else:
          counts[word] = 1 

sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True) 

print(f'===== Text Report =====')
print(f'Words      : {len(words)}')
print(f'Lines      : {len(lines)}')
print(f'Characters : {len(text)}')
print(f'Sentences  : {sentences}')
print(f'=======================')
print('Top 5 most frequent words:')
i = 1
for word, count in sorted_words[:5]:
    print(f'{i}. {word}: {count}')
    i += 1
print(f'=======================')
