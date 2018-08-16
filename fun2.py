import turtle

bgcolor = input("Choose a bacground color: ")
pencolor = input("Choose our pen color: ")
turtle.color(pencolor)
turtle.bgcolor(bgcolor)

ready = str(input("Are you ready to play? ")
            

turtle.goto(0,0)
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = None
print(direction)

def up():
    global direction
    direction = UP
    on_move(0,5)
    print(direction)
    print("You pressed the up key.")

def down():
    global direction
    direction = DOWN
    on_move(0,-5)
    print(direction)
    print("You pressed the down key.")

def left():
    global direction
    direction = LEFT
    on_move(-5,0)
    print(direction)
    print("You pressed the left key.")

def right():
    global direction
    direction = RIGHT
    on_move(5,0)
    print(direction)
    print("You pressed the right key.")

def on_move(x_change, y_change):
    x,y = turtle.pos()
    x_new = x+x_change
    y_new = y+y_change
    turtle.goto(x_new, y_new)

def space():
    if turtle.isdown():
        turtle.penup()
        print("Your pen is now up.")
    else:
        turtle.pendown()
        print("Your pan is now down.")
        

turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(space, " ")
turtle.listen()

turtle.mainloop()
