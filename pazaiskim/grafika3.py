import turtle
s = turtle.Screen()
t = turtle.Turtle()
s.bgcolor('purple')
s.title('mano pirmas kartas')
t.color ('green')
t.pensize(5)
t.speed(0) #0 greiciausias,1 leciausias, 10 greitas
t.fillcolor('red')
t.begin_fill()
for i in range(5):
    t.lt(360/5)
    t.fd(100)
t.end_fill()


s.exitonclick()