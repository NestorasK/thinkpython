# Write a function that reads the file words.txt and builds a list with one
# element per word. Write two versions of this function, one using the append
# method and the other using the idiom t = t + [x].
# Which one takes longer to run? Why?

# %%
def build_list_from_file(filename):
    fin = open(file = filename)
    out_list = []
    for line in fin:
        word = line.strip()
        out_list.append(word)

    return out_list

def build_list_from_file2(filename):
    fin = open(file = filename)
    out_list = []
    for line in fin:
        word = line.strip()
        out_list = out_list + [word]

    return out_list

# %%
# f_list = build_list_from_file(filename="../words.txt")

# # %%
# f_list_2 = build_list_from_file2(filename="../words.txt")


# %%
