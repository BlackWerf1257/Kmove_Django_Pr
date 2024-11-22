import turtle
import random

turtleList=[]
colorList=['red','green','blue','black','magenta','orange','gray','pink']

turtle.shape('turtle')
turtle.screensize(500,500)

for i in range(0,100):
    color=random.choice(colorList)
    x = random.randint(-250,250)
    y = random.randint(-250,250)
    myTurtle = (color, x, y)
    turtleList.append(myTurtle)
                          

for tup in turtleList:
    turtle.pencolor=(tup[0])
    turtle.goto(tup[1],tup[2])
    turtle.color(random.choice(colorList))
    turtle.stamp()

turtle.done()
