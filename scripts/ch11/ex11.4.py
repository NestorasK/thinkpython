def has_duplicates(mylist):
    """Evaluate if there are duplicates using a dictionary
    and a for loop
    """

    mydir = dict()
    for x in mylist:
        print(x)
        if x in mydir:
            return True
        mydir[x] = True
        print(mydir)

    return False


has_duplicates(mylist=['a', 'b', 'c', 'd', 'a'])
