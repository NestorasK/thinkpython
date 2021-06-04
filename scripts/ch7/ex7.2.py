import math
def eval_loop():
    while True:
        line = input('> ')
        if line == "done":
            break
        print(eval(line))
        line_last = line
    print(eval(line_last))

eval_loop()
