# Exercise 11.2. Read the documentation of the dictionary method setdefault
# and use it to write a more concise version of invert_dict.


def invert_dict(d):

    inverse = {}

    for key in d:
        val = d[key]

        # Initiate the position when needed
        inverse.setdefault(val, [])

        # Fills the position
        inverse[val].append(key)

    return inverse


print("Example")
dict_to_inv = {'a': 1, 'b': 1, 'c': 2, 'd': 2}
print(dict_to_inv)
print(invert_dict(dict_to_inv))
