print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
import turtle, random

colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]
painter = turtle.Turtle()
painter.speed(3)
for i in range(10):
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0)
