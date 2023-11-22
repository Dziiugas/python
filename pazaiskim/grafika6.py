import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.goto(0,0)
t.pendown()
for i in range (6):
    t.rt(360/6)
    t.fd(100)
    for j in range (6):
        t.lt(360/6)
        t.fd(100)

    


s.exitonclick()