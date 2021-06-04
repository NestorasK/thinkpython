# Exercise 6.4. A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b. Note: you will have to think about the base case.

def is_power(a, b):

    if a == 0:
        return "A is 0"

    if b == 0:
        return "B is 0"
    
    remainder = a % b
    if remainder == 0:
        remainder2 = (a / b) % b
        if remainder2 == 0:
            return True
        else:
            return False
    else:
        return False


print(is_power(5, 0))

