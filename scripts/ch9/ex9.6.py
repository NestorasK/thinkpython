# Exercise 9.6. Write a function called abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok).
# How many abecedarian words are there?

def abecedarian(word):
    counter = 0
    for letter_i in word:
        if counter == 0:
            counter = counter + 1
            next
        else:
            if letter_i > letter_in:
                next
            else:
                return(False)
        letter_in = letter_i
    return(True)

def words_counter(file_out):
    counter_words = 0
    for line in file_out:
        word = line.strip()
        if abecedarian(word=word):
            counter_words = counter_words + 1
    return(counter_words)


fin = open(file="scripts/ch9/words.txt")
print(words_counter(file_out=fin))

