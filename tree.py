

import turtle


def drawstick(list,len,a,de):
    if len>10:
        l=[]
        for turtle in list:
            
            turtle.forward(len)
            p=turtle.clone()
            p.left(a)
            turtle.right(a)
            l.append(p)
            l.append(turtle)
        drawstick(l,len*de,a,de)
    

def main():
    turtle.pensize(5)
    turtle.color("green")
    turtle.left(90)
    
    drawstick([turtle],100,55,0.7)

main()
    
