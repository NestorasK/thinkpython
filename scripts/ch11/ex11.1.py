# Exercise 11.1. Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

# %%
def read_word(filename):
    word_txt = dict()
    fin = open(file=filename)
    counter = 0
    for line in fin:
        word = line.strip()
        word_txt[word] = counter
    return word_txt

# %%
word_txt_dict = read_word(filename="../words.txt")


# %%
# Create a list
def build_list_from_file(filename):
    fin = open(file = filename)
    out_list = []
    for line in fin:
        word = line.strip()
        out_list.append(word)
    return out_list

f_list = build_list_from_file(filename="../words.txt")

# %%
# Looking into a dictionary
for word_i in f_list[0:100000]:
    out = word_i in word_txt_dict
    # print(word_i, out)


# %%
for word_i in f_list[0:100000]:
    out = word_i in f_list
    # print(word_i, out)



# %%
# If you did Exercise 10.10, you can compare the speed of this implementation with the list in operator and the bisection search.



# %%

