# Exercise 10.1. Write a function called that takes a list of lists of integers and adds up the elements from all of the nested lists. For example:
# t = [[1,2], [3], [4,5,6]]

def nested_sum(t):
    out = 0
    for nested in t:
        out = out + sum(nested)
    return out

inputlist = [[1,2], [3], [4, 5, 6]]
result = nested_sum(t = inputlist)
print(result)
