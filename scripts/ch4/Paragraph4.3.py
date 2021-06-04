import turtle
import math

def square(t, length):
    # print(t)
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()

def polygon(t, length, n):
    #print(t)
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    turtle.mainloop()

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, length, n)

def arc(t, r, n, angle):
    circumference = 2 * math.pi * r
    length = circumference / n
    n_i = int(n * (angle / 360))
    for i in range( n_i ):
        t.fd(length)
        t.lt(360/n)
    turtle.mainloop()


bob = turtle.Turtle()
# square(bob, 150)
# polygon(bob, 100, 7)
# circle(bob, 100, 50)
arc(bob, 100, 360, 90)
