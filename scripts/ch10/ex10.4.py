# Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns

def chop(t):
    del t[0]
    del t[len(t) - 1]
    return (t)

input = [1,2,3,4]
print("input is:", input)
output = chop(t=input)
print("output is:", output, "and input is:", input)
