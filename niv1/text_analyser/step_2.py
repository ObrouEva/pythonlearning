text = """the quick brown fox jumps over the lazy dog 
the dog barked at the fox 
the fox ran away"""

words = text.lower().split()

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1 #word seen before - add 1
    else:
        counts[word] = 1 # word seen for first time - start at 1

sorted_words = sorted(counts.items(), #.item() → converts the dictionarh into a list of tuple -- pairs of (key, value). each tuple is (word, count)
                      key=lambda x: x[1], #lambda x: x[1] means : "for each item x, sort by its second element" — the count.
                      reverse=True) 
# sorted() just sorts a list. Simple.
# Take all (word, count) pairs — sort them by their count — highest first.

print('Top 3 words:')

for word, count in sorted_words[:3]:
    print(f'{word}: {count}')