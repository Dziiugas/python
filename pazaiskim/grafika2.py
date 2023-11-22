import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.color ('green')
for i in range(5):
    t.lt(360/5)
    t.fd(100)

t.circle(60)
t.dot(20)

s.exitonclick()