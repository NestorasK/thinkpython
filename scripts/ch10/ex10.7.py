# Write a function called has_duplicates that takes a list and returns
# True if there is any element that appears more than once.
# It should not modify the original list.

def has_duplicates(t):
    print("input list:", t)
    for i in range(len(t)):
        t_tmp = t[:]
        del t_tmp[i]
        if t[i] in t_tmp:
            return True

    return False

print(has_duplicates(t = ['a', 'b', 'c']))
print(has_duplicates(t = ['a', 'b', 'a']))
print(has_duplicates(t = ['a', 'a', 'a']))
print(has_duplicates(t = ['a', 'b']))

