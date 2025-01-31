import turtle
import random
import time
delay = 0.1
sc = 0
hs = 0
bodies=[]

#creating a screen
s= turtle.Screen()
s.title("Snake Game")
s.bgcolor("light blue")
s.setup(width = 600, height = 600)# this is for setting screen size

# creating a Head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.fillcolor("red")
head.penup()
head.goto(0,0)
head.direction="stop"

# creating a food for snake
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.fillcolor("blue")
food.penup()
food.ht()   # for hiding a turrtle
food.goto(150,200)
food.st()   # for showing a turtle

 #creating a score board
sb = turtle.Turtle()
sb.penup()
sb.shape("square")
sb.ht()
sb.goto(-250,250)
sb.write("Score:0 | Highest Score: 0") # this function used to print a score on the screen for first time

# creating function for moving in all directions
def moveUp():
    if head.direction!="down":
        head.direction="up"

def moveDown():
    if head.direction!="up":
        head.direction="down"

def moveLeft():
    if head.direction!="left":
        head.direction="right"

def moveRight():
    if head.direction!="righ":
        head.direction="left"

def moveStop():
    head.direction!="stop"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#event hanling
s.listen()
s.onkey(moveUp,"Up")
s.onkey(moveDown,"Down")
s.onkey(moveLeft,"Left")
s.onkey(moveRight,"Right")
s.onkey(moveStop,"space")

#mainloop
while True:
    s.update() #to update the secreen
    # check collision with border
    if head.xcor()>290:
        head.setx(-290)

    if head.xcor()<-290:
        head.setx(290)

    if head.ycor()>290:
        head.sety(-290)

    if head.ycor()<-290:
        head.sety(290)
# check collision with food
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #increase the body of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        bodies.append(body) #append the new body in list

        sc = sc+10 #increase the score
        delay = delay-0.0001 # this is use for increase speed

        if sc>hs:
            hs=sc #update highest score
        sb.clear() #to clear score board
        sb.write("Score:{}   | highest Sore:{}".format(sc,hs))
    #move snake bodies
    for i in range(len(bodies)-1,0,-1):
        x=bodies[i-1].xcor()
        y=bodies[i-1].ycor()
        bodies[i].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()
#check collisioo with snake body....
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            sc=0
            delay=0.1
            sb.clear()
            sb.write("Score:{}   |  Highest Score:{}".format(sc,hs))
    time.sleep(delay)
s.mainloop()

            





                 
        
        
