text = 'python is great and python is fun and learning python is the best way to learn python'

words = text.split()

word_count = {} #a dictionary stores key: value pairs
 
for word in words:
    if word in word_count:
      word_count[word] +=1 # is 'python' already in word_count? yes so value + 1
    else:
       word_count[word] = 1

# for word, count in word_count.items():
#     print(f"{word} : {count}")

sorted_words = sorted(word_count.items(), 
                      key=lambda x: x[1], #function in short  #def get_count(x): /n return x[1]
                      # x[0] = the word → 'python' x[1] = theh count → 4
                      reverse=True)

print('Top 3 words')

for word, count in sorted_words[:3]: #[:3] → first 3 items
   print(f'{word} : {count}')


