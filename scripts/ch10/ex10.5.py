# Write a function called is_sorted that takes a list as a parameter and
# returns True if the list is sorted in ascending order and False otherwise.

def is_sorted(t):
    for i in range(len(t)-1):
        if (t[i] < t[i+1]):
            next;
        else:
            return False

    return True

print(is_sorted(t = [1,2,3,4]))
print(is_sorted(t = [2,1,3,4]))
print(is_sorted(t = ['a', 'b']))
print(is_sorted(t = ['b', 'a']))
