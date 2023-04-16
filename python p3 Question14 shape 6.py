import turtle

t = turtle.Turtle()

t.left(60)
t.forward(100)
for j in range(4):
    t.right(120)
    t.forward(100)
    t.left(120)
    t.forward(100)

t.hideturtle()
t.done()





