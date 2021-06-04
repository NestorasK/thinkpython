def check_fermat(a, b, c, n):
    """
    Evaluate fermat Last Theorem
    a: int
    b: int
    c: int
    n: number greater than 2
    """
    
    if (a^n + b^n == c^n) and (n > 2) :
        print("Holy smokes, Fermat was wrong!")
    else: 
        print("No, that doesn’t work.")

def userInput():
    """
    Ask the user to provide four numbers and 
    calls check_fermat function
    """
    a_i = input("Provide a\n")
    a_i = int(a_i)
    b_i = input("Provide b\n")
    b_i = int(b_i)
    c_i = input("Provide c\n")
    c_i = int(c_i)
    
    n_i = input("Provide n\n")
    n_i = int(n_i)

    print("Checking fermat Last Theorem...")
    check_fermat(a_i, b_i, c_i, n_i)




userInput()

