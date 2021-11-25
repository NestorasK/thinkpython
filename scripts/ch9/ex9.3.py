# Write a function named avoids that takes a word and a string of forbidden letters, and that returns True if the word doesn’t use any of the forbidden letters. Write a program that prompts the user to enter a string of forbidden letters and then prints the number of words that don’t contain any of them.
# Can you find a combination of 5 forbidden letters that excludes the smallest number of words?

def avoids(word, string):
    for letter in word:
        if letter in string:
            return(False)
    else:
        return(True)

def words_counter(file_out, user_input):
    counter_words = 0
    for line in file_out:
        word = line.strip()
        if avoids(word=word, string=user_input):
            # print(word)
            counter_words = counter_words + 1

    return(counter_words)

user_input = input("Give me five letters\n")
fin = open("scripts/ch9/words.txt")

print(
    "Number of words not containing the letters:",
    user_input,"\n",
    words_counter(file_out=fin, user_input=user_input)
)













