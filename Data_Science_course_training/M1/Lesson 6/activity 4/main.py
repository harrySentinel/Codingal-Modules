import turtle

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

pen = turtle.Turtle()
pen.speed(0)
turtle.bgcolor("black")

for i in range(200):
    pen.color(colors[i % len(colors)])
    pen.forward(i * 0.5)
    pen.left(59)

turtle.done()
