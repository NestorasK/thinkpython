# Exercise 9.4. Write a function named "uses_only" that takes a word and a string of letters, and that returns True if the word contains only letters in the list.
# Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa”?
#%%
def uses_only(word, allowed_letters):
    """Returns true if the word is made only from the allowed letters
    """
    for letter_i in word:
        if letter_i in allowed_letters:
            next
        else:
            return(False)
    return(True)
#%%
mytest = "nestors"
print(uses_only(word="nestor", allowed_letters="nr"))

# %%
