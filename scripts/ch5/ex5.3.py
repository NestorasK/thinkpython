def is_triangle(a, b, c):
    """
    Evaluate if a triangle can be formed
    a: int
    b: int
    c: int
    """
    
    a_b = a + b
    a_c = a + c
    b_c = b + c


    if (a_b < c) or (a_c < b) or (b_c < a):
        print("No")
    else:
        print("Yes")


def userInput():
    """
    Ask the user to provide three numbers and 
    calls is_triangle function
    """
    a_i = input("Provide a\n")
    a_i = int(a_i)
    b_i = input("Provide b\n")
    b_i = int(b_i)
    c_i = input("Provide c\n")
    c_i = int(c_i)
    

    print("Checking if a triangle can be formed...")
    is_triangle(a_i, b_i, c_i)


userInput()
