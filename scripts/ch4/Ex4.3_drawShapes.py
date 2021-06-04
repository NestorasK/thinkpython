import turtle
import polygon
import math

bob = turtle.Turtle()


def isosceles(t, r, angle):
    """
    Draw an isosceles triangle
    t: turtle
    r: length of scele
    angle: half peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)
    t.fd(r)
    angle_base = 180 - ((180 - 2 * angle) / 2)
    t.lt( angle_base )
    t.fd(2*y)
    t.lt( angle_base )
    t.fd(r)
    t.lt( 180 - angle * 2 )
    

def draw_pie(t, r, n):
    """
    draw polygons 
    t: turtle object
    r: radius
    n: number of sides
    """
    angle_i = 360 / (n * 2)
    for i in range(n):
        isosceles(t, r, angle_i)
        t.lt(angle_i * 2)
    

#draw_pie(bob, 50, 4)
#draw_pie(bob, 50, 5)
# draw_pie(bob, 50, 6)
draw_pie(bob, 50, 7)


bob.hideturtle()
# wait for the user to close the window
turtle.mainloop()
