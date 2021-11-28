# Write a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

def middle(t):
    out = t[1:(len(t)-1)]
    return out

input = [1,2,3]
output = middle(t = input)

print("output is:", output)
print("input is:", input)
