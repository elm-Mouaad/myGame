from turtle import *
from random import randint 
import time
#the game screen
game_screen = Screen()
game_screen.title("Game")
game_screen.setup(width=800 , height=600)
game_screen.tracer(0)
game_screen.bgcolor("black")

#the cadre
cadre1 = Turtle()
cadre1.shape("square")
cadre1.speed(0)
cadre1.shapesize(stretch_wid=30 , stretch_len=1)
cadre1.color("purple")
cadre1.penup()
cadre1.goto(390,0)

cadre2 = Turtle()
cadre2.shape("square")
cadre2.speed(0)
cadre2.shapesize(stretch_wid=30 , stretch_len=1)
cadre2.color("purple")
cadre2.penup()
cadre2.goto(-390,0)

cadre3 = Turtle()
cadre3.shape("square")
cadre3.speed(0)
cadre3.shapesize(stretch_wid=1 , stretch_len=40)
cadre3.color("purple")
cadre3.penup()
cadre3.goto(0,290)

cadre4 = Turtle()
cadre4.shape("square")
cadre4.speed(0)
cadre4.shapesize(stretch_wid=1 , stretch_len=40)
cadre4.color("purple")
cadre4.penup()
cadre4.goto(0,-290)

# the snack head  
head = Turtle()
head.shape("square")
head.color("white")
head.speed(0)
head.penup()
head.goto(0,0)
switshx = 10
switshy = 0

segment = []

#the fruite 
x_fruite = randint(-370,370)
y_fruite = randint(-270,270)
fruite = Turtle()
fruite.shape("square")
fruite.color("aqua")
fruite.penup()
fruite.speed(0)
fruite.shapesize(stretch_len=0.5,stretch_wid=0.5)
fruite.goto(x_fruite,y_fruite)


def head_move() :
    head.setx(head.xcor()+switshx)
    head.sety(head.ycor()+switshy)
def mouve_up() :
    global switshx
    global switshy
    switshx = 0
    switshy = 10
def mouve_down() :
    global switshx
    global switshy
    switshx = 0
    switshy = -10
def mouve_right() :
    global switshx
    global switshy
    switshx = 10
    switshy = 0
def mouve_left() :
    global switshx
    global switshy
    switshx = -10
    switshy = 0
    
game_screen.listen()
game_screen.onkeypress(mouve_up, "Up")
game_screen.onkeypress(mouve_down, "Down")
game_screen.onkeypress(mouve_right, "Right")
game_screen.onkeypress(mouve_left, "Left")
con = 0
while con !=1 :
    game_screen.update()
    if x_fruite - 10 <= head.xcor() <= x_fruite + 10 and y_fruite - 10 <= head.ycor() <= y_fruite + 10 :
        fruite.clear()
        x_fruite = randint(-370,370)
        y_fruite = randint(-270,270)
        fruite.goto(x_fruite,y_fruite)

        new_segment = Turtle()
        new_segment.color("aqua")
        new_segment.penup()
        new_segment.speed(0)
        new_segment.shape("square")
        segment.append(new_segment)

    elif head.xcor()<=-380 or head.xcor()>=380 or head.ycor()>=280 or head.ycor()<=-280 :
        time.sleep(1)
        break
    for index in range(len(segment)-1 , 0 , -1) :
        x = segment[index-1].xcor()
        y = segment[index-1].ycor()
        segment[index].goto(x,y)
    if len(segment)>0 :
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x,y)
    time.sleep(0.04)
    head_move()
    for seg in segment :
        if seg.distance(head) < 10 :
            time.sleep(1)
            con = 1
            break



game_screen.clear()
game_screen.bgcolor("black")
game_over = Turtle()
game_over.color("aqua")   
game_over.penup()
game_over.shape("square")
game_over.speed(0)
game_over.hideturtle()
game_over.goto(0,0)
game_over.write( "game over" , align="center" , font=("italic" , 30 , "bold"))
game_screen.mainloop()
    
