# Exercise 9.5.
# Write a function named "uses_all" that takes a word and a string of required letters, and that returns True if the word uses all the required letters at least once. How many words are there that use all the vowels aeiou? How about aeioy?

def uses_all(word, required_letters):
    """Returns true if the word uses all the required letters
    """
    for letter_i in required_letters:
        if letter_i in word:
            next
        else:
            return(False)
    return(True)


def words_counter(file_out, user_input):
    counter_words = 0
    for line in file_out:
        word = line.strip()
        if uses_all(word=word, required_letters=user_input):
            print(word)
            counter_words = counter_words + 1

    return(counter_words)

fin = open("scripts/ch9/words.txt")
user_input = input("Give me five letters\n")


print(
    "Number of words containing the required letters:",
    user_input,"\n",
    words_counter(file_out=fin, user_input=user_input)
)



