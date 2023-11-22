import turtle
s = turtle.Screen()
t = turtle.Turtle()
colors=['yellow','red','cyan','green']
t.penup()
t.goto(-300,0)
t.pendown()
t.speed(1)
for j in range (4):
    t.pencolor(colors[j%len(colors)])
    for i in range (j,4,4):
        t.lt(360/4)
        t.fd(100)
t.penup()
t.goto(-100,0)
t.pendown()
t.speed(1)
for j in range (4):
    t.pencolor(colors[j%len(colors)])
    for i in range (j,4,4):
        t.lt(360/4)
        t.fd(100)
t.penup()
t.goto(50,0)
t.pendown()
t.speed(1)
for j in range (4):
    t.pencolor(colors[j%len(colors)])
    for i in range (j,4,4):
        t.lt(360/4)
        t.fd(100)
t.penup()
t.goto(200,0)
t.pendown()
t.speed(1)
for j in range (4):
    t.pencolor(colors[j%len(colors)])
    for i in range (j,4,4):
        t.lt(360/4)
        t.fd(100)
t.penup()
t.goto(400,0)
t.pendown()
t.speed(1)
for j in range (4):
    t.pencolor(colors[j%len(colors)])
    for i in range (j,4,4):
        t.lt(360/4)
        t.fd(100)


s.exitonclick()