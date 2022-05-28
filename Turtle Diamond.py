import turtle

t = turtle.Pen()
turtle.bgcolor('black')
t.speed(11)

colors = ['red','yellow','green','purple','blue','orange']

for x in range(200):
    t.pencolor(colors[x%6])
    t.width(x/50+1)
    t.forward(x)
    t.lt(100)
