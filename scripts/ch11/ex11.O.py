# Exercises suggested in text.


def histogram(s):
    # histogram function from the book
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def histogram2(s):
    # histogram function using gets
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


h = histogram('parrot')
print("\nh is:", h)

h2 = histogram2('parrot')
print("\nh2 is:", h2)
