import turtle
import polygon

bob = turtle.Turtle()

def petal(t, r, angle):
    """Draws a petal with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    polygon.arc(t, r, angle)
    bob.lt( 180 - angle )
    polygon.arc(bob, r, angle)

def flower(t, r, angle, numPetals):
    angle_petals = (180 - angle) + (360 / numPetals)
    for i in range(numPetals):
        petal(t, r, angle)
        t.lt( angle_petals )

flower(bob, 150, 30, 20)


# wait for the user to close the window
turtle.mainloop()
