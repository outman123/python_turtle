


import turtle

turtle.pensize(7)
turtle.color("yellow")

turtle.penup()    
turtle.goto(0,200)   
turtle.pendown()
for i in range(5):
    turtle.forward(100)
    turtle.right(144)

    
turtle.hideturtle()
    
turtle.penup()    
turtle.goto(-50,100)   
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(20)
turtle.end_fill()

turtle.penup()    
turtle.goto(150,100)   
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(20)
turtle.end_fill()


turtle.penup()    
turtle.goto(0,0)   
turtle.pendown()
turtle.color("red")
turtle.forward(100)

turtle.penup()    
turtle.goto(50,-80)   
turtle.pendown()
turtle.color("black")
turtle.circle(200)



