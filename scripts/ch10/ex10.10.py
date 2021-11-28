# %%
import math
from ex10_9 import build_list_from_file

def in_bisect(t, stri):
    # print("\nt is:", t)
    # print("stri is:", stri)
    if t == []:
        # print("Here")
        return False

    if len(t) == 2:
        if stri == t[0] or stri == t[1]:
            return True
        else:
            return False

    pointer_start = 0
    # print("pointer_start =", pointer_start, t[pointer_start])
    pointer_end = len(t) - 1
    # print("pointer_end =", pointer_end, t[pointer_end])
    pointer_middle = math.floor((pointer_end + pointer_start) / 2)
    # print("pointer_middle =", pointer_middle, t[pointer_middle])

    if stri == t[pointer_middle]:
        return True
    else:
        if stri < t[pointer_middle]:
            return in_bisect(t = t[pointer_start:(pointer_middle+1)], stri=stri)
        elif stri > t[pointer_middle]:
            return in_bisect(t = t[(pointer_middle):pointer_end+1], stri=stri)

# %%
f_list = build_list_from_file(filename="words.txt")

# %%

for word_i in f_list:
    out = in_bisect(t = f_list, stri = word_i)
    print(word_i, out)
    if out == False:
        print("Something is wrong")
        break

