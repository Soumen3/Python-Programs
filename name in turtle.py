import random
import turtle as t
t.pen()
t.bgcolor('black')
colors=['red','green','yellow','blue','gray','purple','aqua','brown']
name=t.textinput('Fill the details','Eneter your text')
s=int(t.numinput('Number of sides','How many sides you want',10,1,20))
for i in range(70):
    t.pencolor(random.choice(colors))
    t.penup()
    t.forward(i*5)
    t.pendown()
    t.write(name,font=('',int((i*2+4)/4),'bold'))
    t.left(360/s+4)
