# Exercise 10.2. Write a function called cumsum
# that takes a list of numbers and returns the cumulative sum;
# that is, a new list where the ith element is the sum of the
# first i + 1 elements from the original list. For example:

def cumsum(t):
    cumsum_out = []
    for i in range(len(t)):
        if i == 0:
            x = t[i]
        else:
            x = x + t[i]
        cumsum_out.append(x)

    return(cumsum_out)

inlist = [1, 5, 7]
print("final out:", cumsum(t = inlist))
