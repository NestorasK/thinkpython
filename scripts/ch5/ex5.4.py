def recurse(n, s):
    if n == 0:
        print(s)
    else:
        # print("s:", s)
        # print("n:", n)
        recurse(n-1, n+s)


recurse(5, 0)
