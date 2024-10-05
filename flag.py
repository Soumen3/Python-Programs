import turtle 
colors=["green","white","orange"]
turtle.bgcolor("black")
for i in range(200):
    turtle.pencolor(colors[i%3])
    turtle.width(i/100+1)
    turtle.forward(i)
    turtle.left(59)