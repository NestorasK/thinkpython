# In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter “e”. Since “e” is the most common letter in English, that’s not easy to do. In fact, it is difficult to construct a solitary thought without using that most common symbol. It is slow going at first, but with caution and hours of training you can gradually gain facility. All right, I’ll stop now.
# Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.
# Write a program that reads words.txt and prints only the words that have no “e”. Compute the percentage of words in the list that have no “e”.

def has_no_e(word):
    if "e" in word:
        return(False)
    else:
        return(True)

fin = open(file="scripts/ch9/words.txt")
counter_words_no_e = 0
counter_words = 0

for line in fin:
    word = line.strip()
    if has_no_e(word=word):
        print(word)
        counter_words_no_e = counter_words_no_e + 1
    counter_words = counter_words + 1

percent = (counter_words_no_e / counter_words) * 100
print("\n\nPercent of words without e:\n", percent, "\n")








