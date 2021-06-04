import math
def mysqrt(a):
    x = a
    while True:
        # print(x)
        y = (x + a/x) / 2
        if abs(y - x) < 10**(-16):
            break
        x = y
    return x

def test_square_root():
    print("a", "mysqrt(a)", "math.sqrt(a)", "diff")
    print("-", "---------", "------------", "----")
    for a in range(1, 10):
        print(a, mysqrt(a), math.sqrt(a), abs(math.sqrt(a) - mysqrt(a)))

test_square_root()
