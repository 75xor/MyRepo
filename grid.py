x=0
y=0
c=0
import turtle
while(c<25):
	turtle.goto(x,y)
	turtle.pendown()
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.penup()
	c+=1
	x+=100
	if(x>400):
		x=0
		y+=100
turtle.exitonclick()

		

