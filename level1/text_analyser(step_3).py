text = """Python is great. 
Learning Python is fun.
Python is used in cybersecurity.
Every hacker knows Python. """

char_count = len(text)
line_count = len(text.split('\n'))
words_count = len(text.lower().split())  # ← no argument, handles all whitespace 
# .lower() -> stripping punctuation from each word
sentence_count = len(text.split('.')) - 1

words = text.lower().split()

word_count = {} #

for word in words:
    if word in word_count:
      word_count[word] +=1 # is 'python' already in word_count? yes so value + 1
    else:
       word_count[word] = 1
  

sorted_words = sorted(word_count.items(), 
                      key=lambda x: x[1])#function in short  #def get_count(x): /n return x[1]
                      # x[0] = the word → 'python' x[1] = theh count → 4
unique = len(set(words)) #set() removes duplicates automatically

print(f'--- Text Report ---\nCharacters  : {char_count}\nWords       : {words_count}\nLines       : {line_count}\nSentences   : {sentence_count}\nUnique words: {unique}')
