def do_four(fun, arg_i):
    do_twice(fun, arg_i)
    do_twice(fun, arg_i)

def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def print_spam():
    print('spam')

# do_twice(print_twice, 'spam')
do_four(print_twice, "scam")
