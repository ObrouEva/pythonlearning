# Step 1 — Read the file
with open('/Users/ATOM/python learning/level1/sample.txt', 'r') as f:
    text = f.read()

# Step 2 — Analysis (exactly what you had before)
char_count = len(text)
line_count = len(text.split('\n'))
words_count = len(text.lower().split())
sentence_count = len(text.split('.')) - 1
words = text.lower().split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

unique = len(set(words))
sorted_words = sorted(word_count.items(), 
                      key=lambda x: x[1],
                      reverse=True)

     
# 'r'  → file already exists, you read from it
# 'w'  → creates the file if it doesn't exist, you write to it
# 'a'  → file already exists, you add to the end of it

with open('/Users/ATOM/python learning/level1/report.txt', 'w') as f:
    f.write('=============================\n')
    f.write('     TEXT ANALYSIS REPORT    \n')
    f.write('=============================\n')
    f.write(f'Characters  : {char_count}\n')
    f.write(f'Words       : {words_count}\n')
    f.write(f'Lines       : {line_count}\n')
    f.write(f'Sentences   : {sentence_count}\n')
    f.write(f'Unique words: {unique}\n')
    f.write('\n')
    f.write('Top 5 most frequent words :\n')
    for i, (word, count) in enumerate(sorted_words[:5], 1):
      f.write(f'{i}. {word} : {count}\n')
    f.write('=============================\n')