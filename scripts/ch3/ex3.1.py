def right_justify(s):
    numSpaces = 70 - len(s)
    cat = " "*numSpaces + s
    print(cat)

right_justify('test')
