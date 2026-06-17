import turtle

pen = turtle.Turtle()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(36):
    pen.color(colors[i % 6])
    pen.forward(i * 5)
    pen.right(60)

turtle.done()
