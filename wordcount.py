"""
wordcounter program

wordcount.py opens a file, and counts how many times each space-separated
word occurs in that file. The output prints those counts to the screen.
"""
input_file = open("test.txt")
word_count = {}   

for line in input_file:
    stripped_line = line.rstrip()
    #print line
    words = stripped_line.split(" ")



# iterate over the number of words in the list of words
# then add each word to the dictionary word_count and its value
# update the value if you encounter the word another time

    for word in words:
        #print "word: ", word
        #print "word_count: ", word_count
        current_count = word_count.get(word, 0)
        word_count[word] = current_count + 1
        #print word, word_count[word]

#option 1 - preferred
#for key, value in word_count.items():
#    print key, value

#option 2 - works but creates a new list in memory
# might use .keys() if you wanted to sort your keys
#for key_word in word_count.keys():
#    print key_word, word_count[key_word]

#option 3 doesn't create a new list in memory
for key_word in word_count:
    print key_word, word_count[key_word]

