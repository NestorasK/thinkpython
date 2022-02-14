# Exercise 11.3. Memoize the Ackermann function from Exercise 6.2 and see if
# memoization makes it possible to evaluate the function with bigger arguments.

cache = {}


def ack(m, n):

    # print("cache in:", cache)

    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        # print("Here", m, n)
        return ack(m-1, 1)

    if (m, n) in cache:
        # print("return cache")
        return cache[m, n]
    else:
        # print("filling cache")
        cache[m, n] = ack(m-1, ack(m, n-1))
        # print("cache", cache)

        return cache[m, n]


print(ack(3, 4))
print(ack(3, 7))
print(ack(3, 8))
