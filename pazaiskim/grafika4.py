import turtle
s = turtle.Screen()
t = turtle.Turtle()
colors=['BlueViolet','Cyan','Chocolate','Chartreuse','DeepPink','FireBrick','Indigo']
x = len(colors) - 3
t.color ('green')
t.penup()
t.goto(0,-390)
t.pendown()
for j in range (13,2,-1):
    t.pencolor(colors[(j+4)%len(colors)])
    t.fillcolor(colors[j%len(colors)])
    t.begin_fill()
    for i in range(j):
        t.lt(360/j)
        t.fd(100)
    t.end_fill()




s.exitonclick()