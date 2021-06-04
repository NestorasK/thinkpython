import turtle
import polygon


ida = turtle.Turtle()

def draw_a(t):
    t.lt(60)
    t.fd(40)
    t.right(60)
    polygon.polygon(t, 3, 50)
    t.fd(50)
    t.rt(60)
    t.fd(40)

def draw_b(t):
    t.fd(4)
    polygon.arc(t, 20, 180)
    t.lt(180)
    polygon.arc(t, 20, 180)
    t.fd(4)
    t.lt(90)
    t.fd(80)

def draw_c(t):
    """
    docstring
    """
    t.lt(180)
    t.fd(4)
    polygon.arc(t, 40, 180)
    t.fd(4)

def draw_d(t):
    """
    docstring
    """
    t.fd(4)
    polygon.arc(t, 40, 180)
    t.fd(4)
    t.lt(90)
    t.fd(80)

def draw_e(t):
    """
    docstring
    """
    t.fd(50)
    t.lt(180)
    t.fd(50)
    
    t.rt(90)
    t.fd(40)
    t.rt(90)
    
    t.fd(40)
    t.lt(180)
    t.fd(40)

    t.rt(90)
    t.fd(40)
    t.rt(90)
    t.fd(50)
    
def draw_f(t):
    """
    docstring
    """
    
    t.lt(90)
    t.fd(40)
    t.rt(90)
    
    t.fd(40)
    t.lt(180)
    t.fd(40)

    t.rt(90)
    t.fd(40)
    t.rt(90)
    t.fd(50)


def draw_g(t):
    """
    docstring
    """

    t.lt(180)
    t.fd(10)
    polygon.arc(t, 50, 180)
    t.fd(10)

    t.lt(90)
    t.fd(40)
    t.lt(90)
    t.fd(20)

def draw_h(t):
    """
    docstring
    """

    t.lt(90)
    t.fd(100)
    t.lt(180)
    t.fd(50)
    
    t.lt(90)
    t.fd(40)

    t.lt(90)
    t.fd(50)
    t.rt(180)
    t.fd(100)

def draw_i(t):
    """
    docstring
    """
    t.lt(90)
    t.fd(100)


def draw_j(t):
    """
    docstring
    """
    t.rt(90)
    polygon.arc(t, 10, 180)
    t.fd(100)

def draw_k(t):
    """
    docstring
    """
    t.lt(90)
    t.fd(50)
    t.rt(140)
    t.fd(60)
    t.rt(180)
    t.fd(60)
    t.rt(90)
    t.fd(50)
    t.rt(180)
    t.fd(50)
    t.rt(130)
    t.fd(50)






draw_k(ida)


# wait for the user to close the window 
turtle.mainloop()
