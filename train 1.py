import turtle
turtle.penup()
turtle.setx(-180) #change the position of the x coordinate

turtle.speed(20)
#create the 1st rectangle
turtle.color("black","blue")
turtle. begin_fill()
turtle.pendown()
turtle.forward(80)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle. forward(80)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.end_fill()
turtle.forward(80)

#create the 2nd rectangle
turtle.color("black","orange")
turtle.begin_fill()
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.end_fill()
turtle.forward(130)

#create the first 2 small wheels
turtle.color("black","green")
turtle.begin_fill()
turtle.right(180)
turtle.forward(20)
turtle.right(90)
turtle.circle(10)
turtle.right(270)
turtle.forward(25)
turtle.right(90)
turtle.circle(10)
turtle.right(270)
turtle.end_fill()
turtle.forward(40)
turtle.penup()

#create the large wheel
turtle.color("black","pink")
turtle.begin_fill()
turtle.right(60)
turtle.pendown()
turtle.circle(20)
turtle.right(300)
turtle.end_fill()

#create the line connecting the carts
turtle.forward(60)

#creat 3rd rectangle
turtle.color("black","yellow")
turtle.begin_fill()
turtle.pendown()
turtle.forward(95)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.end_fill()
turtle.forward(10)

#create the next 3 small wheels
turtle.color("black","brown")
turtle.begin_fill()
turtle.left(180)
turtle.forward(0)
turtle.left(90)
turtle.circle(10)

turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.circle(10)

turtle.right(90)
turtle.forward(5)
turtle.right(90)
turtle.circle(10)

turtle.left(90)
turtle.end_fill()

#create the line connecting the carts
turtle.forward(60)

#create 4th rectangle
turtle.color("black","indigo")
turtle.begin_fill()
turtle.pendown()
turtle.forward(95)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.end_fill()
turtle.forward(10)

#create the last 3 small wheels
turtle.color("black","violet")
turtle.begin_fill()
turtle.left(180)
turtle.forward(0)
turtle.left(90)
turtle.circle(10)

turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.circle(10)

turtle.right(90)
turtle.forward(5)
turtle.right(90)
turtle.circle(10)
turtle.end_fill()
