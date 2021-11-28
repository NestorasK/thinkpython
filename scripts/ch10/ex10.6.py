# Two words are anagrams if you can rearrange the letters from one to spell
# the other. Write a function called is_anagrams that takes two strings and
# returns True if they are anagrams.


def is_anagram(str_i, str_j):
    if len(str_i) != len(str_j):
        return False

    # str_j to list
    str_j_list = list(str_j)

    for letter_i in str_i:
        if letter_i in str_j_list:
            for j in range(len(str_j_list)):
                if str_j_list[j] == letter_i:
                    del str_j_list[j]
                    break;
        else:
            return False
    return True

print(is_anagram(str_i="test", str_j = "este"))

