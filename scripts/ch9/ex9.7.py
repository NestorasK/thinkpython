# Give me a word with three consecutive double letters. I’ll give you a couple of words that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i- p-p-i. If you could take out those i’s it would work. But there is a word that has three consecutive pairs of letters and to the best of my knowledge this may be the only word. Of course there are probably 500 more but I can only think of one. What is the word?

#%%
def is_consecutive(word):
    """ Checks if the word has three consecutive double letters
    word: string
    """

    counter_consec = 0
    i = 0
    while i < (len(word) - 1):
        if word[i] == word[i+1]:
            counter_consec = counter_consec + 1
            if counter_consec == 3:
                return(True)
            i = i + 2
        else:
            i = i + 1
            counter_consec = 0

    return(False)

def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.

    word: string
    returns: bool
    """
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2*count
            count = 0
    return False


def words_counter(file_out):
    counter_words = 0
    for line in file_out:
        word = line.strip()
        if is_triple_double(word=word):
            print(word)
            counter_words = counter_words + 1
    return(counter_words)

fin = open(file = "/Users/nxk070/Documents/Lessons/Learning_Python/thinkpython/scripts/ch9/words.txt")
print(words_counter(file_out=fin))


#%%
