import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n-1)
    t.lt(2*angle)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length*n)

ida = turtle.Turtle()
draw(ida, 50, 2)

turtle.mainloop()
