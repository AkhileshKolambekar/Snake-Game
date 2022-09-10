# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:12:23 2021

@author: Akhilesh
"""

import turtle
import time
import random
score1 = 0
high_score1 = 0
score2 = 0
high_score2 = 0
delay = 0.08
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("blue")
win.setup(width=600,height = 600)
win.tracer(0)

snakehead1 = turtle.Turtle()
snakehead1.shape("circle")
snakehead1.color("green")
snakehead1.penup()
snakehead1.goto(-25,100)
snakehead1.speed(0)
snakehead1.direction = "stop"

snakehead2 = turtle.Turtle()
snakehead2.shape("circle")
snakehead2.color("orange")
snakehead2.penup()
snakehead2.goto(25,100)
snakehead2.speed(0)
snakehead2.direction = "stop"

def movement1():
        if snakehead1.direction == "up":
            y = snakehead1.ycor()
            snakehead1.sety(y+20)
        if snakehead1.direction == "down":
            y = snakehead1.ycor()
            snakehead1.sety(y-20)
        if snakehead1.direction == "right":
            x = snakehead1.xcor()
            snakehead1.setx(x+20)
        if snakehead1.direction == "left":
            x = snakehead1.xcor()
            snakehead1.setx(x-20)

def movement2():
        if snakehead2.direction == "up":
            y = snakehead2.ycor()
            snakehead2.sety(y+20)
        if snakehead2.direction == "down":
            y = snakehead2.ycor()
            snakehead2.sety(y-20)
        if snakehead2.direction == "right":
            x = snakehead2.xcor()
            snakehead2.setx(x+20)
        if snakehead2.direction == "left":
            x = snakehead2.xcor()
            snakehead2.setx(x-20)

def go_up1():
    if snakehead1.direction != "down":
        snakehead1.direction = "up"
def go_down1():
    if snakehead1.direction != "up":
        snakehead1.direction = "down" 
def go_right1():
    if snakehead1.direction != "left":
        snakehead1.direction = "right"
def go_left1():
    if snakehead1.direction != "right":
        snakehead1.direction = "left"

def go_up2():
    if snakehead2.direction != "down":
        snakehead2.direction = "up" 
def go_down2():
    if snakehead2.direction != "up":
        snakehead2.direction = "down" 
def go_right2():
    if snakehead2.direction != "left":
        snakehead2.direction = "right" 
def go_left2():
    if snakehead2.direction != "right":
        snakehead2.direction = "left"

win.listen()

win.onkey(go_up1, "w")
win.onkey(go_down1, "s")
win.onkey(go_right1, "d")
win.onkey(go_left1, "a")

win.onkey(go_up2, "i")
win.onkey(go_down2, "k")
win.onkey(go_right2, "l")
win.onkey(go_left2, "j")

food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(random.randint(-280,280),random.randint(-280,220))

speed_decrease = turtle.Turtle()
speed_decrease.speed(0)
speed_decrease.shape("triangle")
speed_decrease.color("white")
speed_decrease.penup()
speed_decrease.shapesize(0.50, 0.50)
speed_decrease.goto(1000,1000)
speed_decrease.hideturtle()

def speed_down():
    speed_decrease.showturtle()
    speed_decrease.goto(random.randint(-280,280),random.randint(-280,220))
for i in range(50):
    win.ontimer(speed_down,t = 15000*(i+1))

speed_increase = turtle.Turtle()
speed_increase.speed(0)
speed_increase.shape("triangle")
speed_increase.color("cyan")
speed_increase.penup()
speed_increase.shapesize(0.50, 0.50)
speed_increase.goto(1000,1000)
speed_increase.hideturtle()

def speed_up():
    speed_increase.showturtle()
    speed_increase.goto(random.randint(-280,280),random.randint(-280,220))
for i in range(50):
    win.ontimer(speed_up,t = 15000*(i+1))

teleport = turtle.Turtle()
teleport.speed(0)
teleport.shape("triangle")
teleport.color("purple")
teleport.penup()
teleport.shapesize(0.50, 0.50)
teleport.goto(1000,1000)
teleport.hideturtle()

def tel_power():
    teleport.showturtle()
    teleport.goto(random.randint(-280,280),random.randint(-280,220))
for i in range(50):
    win.ontimer(tel_power,t = 15000*(i+1))

invert = turtle.Turtle()
invert.speed(0)
invert.shape("triangle")
invert.color("black")
invert.penup()
invert.shapesize(0.50, 0.50)
invert.hideturtle()

def inv_power():
    invert.showturtle()
    invert.goto(random.randint(-280,280),random.randint(-280,220))
for i in range(50):
    win.ontimer(inv_power,t = 15000*(i+1))

segments1 = []

segments2 = []

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.shape("square")
pen1.color("white")
pen1.penup()
pen1.hideturtle()
pen1.goto(0, 260)
pen1.write("P1 Score : 0  High Score : 0",align = "center",font = ("Courier",24,"normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 230)
pen2.write("P2 Score : 0  High Score : 0",align = "center",font = ("Courier",24,"normal"))

end = turtle.Turtle()
end.speed(0)
end.shape("square")
end.color("white")
end.penup()
end.hideturtle()
end.goto(0, 100)

result = turtle.Turtle()
result.speed(0)
result.shape("square")
result.color("white")
result.penup()
result.hideturtle()
result.goto(0, 0)
    
while True:
    win.update()
    
    if snakehead1.distance(food)<15:
        x = random.randint(-280,280)
        y = random.randint(-280,220)
        food.goto(x,y)
        
        new_segment1 = turtle.Turtle()
        new_segment1.speed(0)
        new_segment1.shape("circle")
        new_segment1.color("green")
        new_segment1.penup()
        segments1.append(new_segment1) 
        score1 += 10
        if score1> high_score1:
            high_score1 = score1
        pen1.clear()
        pen1.write("P1 Score : {}  High Score : {}".format(score1,high_score1),align = "center",font = ("Courier",24,"normal")) 
    
    if snakehead2.distance(food)<15:
        x = random.randint(-280,280)
        y = random.randint(-280,220)
        food.goto(x,y)
        
        new_segment2 = turtle.Turtle()
        new_segment2.speed(0)
        new_segment2.shape("circle")
        new_segment2.color("orange")
        new_segment2.penup()
        segments2.append(new_segment2)
        score2 += 10
        if score2> high_score2:
            high_score2 = score2
        pen2.clear()
        pen2.write("P2 Score : {}  High Score : {}".format(score2,high_score2),align = "center",font = ("Courier",24,"normal"))
    
    elif snakehead1.distance(teleport)<15:
        time.sleep(0.35)
        x = random.randint(-250,250)
        y = random.randint(-250,220)
        snakehead1.goto(x,y)
        teleport.hideturtle()
    
    elif snakehead2.distance(teleport)<15:
        time.sleep(0.35)
        x = random.randint(-250,250)
        y = random.randint(-250,220)
        snakehead2.goto(x,y)
        teleport.hideturtle()
    
    elif snakehead1.distance(invert)<15:
        win.onkey(go_up1, "s")
        win.onkey(go_down1, "w")
        win.onkey(go_right1, "a")
        win.onkey(go_left1, "d")
        invert.hideturtle()
    
    elif snakehead2.distance(invert)<15:
        win.onkey(go_up2, "k")
        win.onkey(go_down2, "i")
        win.onkey(go_right2, "j")
        win.onkey(go_left2, "l")
        invert.hideturtle()
    
    elif snakehead1.distance(speed_decrease)<15:
        delay = 0.15 
        speed_decrease.hideturtle()
        
    elif snakehead2.distance(speed_decrease)<15:
        delay = 0.15 
        speed_decrease.hideturtle()
    
    elif snakehead1.distance(speed_increase)<15 :
        delay = 0.05
        speed_increase.hideturtle()
        
    elif snakehead2.distance(speed_increase)<15 :
        delay = 0.05
        speed_increase.hideturtle()
        
    for index in range(len(segments1)-1, 0, -1):
        x1 = segments1[index-1].xcor()
        y1 = segments1[index-1].ycor()
        segments1[index].goto(x1, y1)
    
    for index in range(len(segments2)-1, 0, -1):
        x2 = segments2[index-1].xcor()
        y2 = segments2[index-1].ycor()
        segments2[index].goto(x2, y2)
    
    if len(segments1)> 0:
        x1 = snakehead1.xcor()
        y1 = snakehead1.ycor()
        segments1[0].goto(x1, y1)
    
    if len(segments2)> 0:
        x2 = snakehead2.xcor()
        y2 = snakehead2.ycor()
        segments2[0].goto(x2, y2)
   
    if snakehead1.xcor() > 290 or snakehead1.xcor() < -290 or snakehead1.ycor() > 290 or snakehead1.ycor() < -290:
        time.sleep(0.1)
        snakehead1.goto(-25, 100)
        snakehead1.direction = "stop" 
        for segment in segments1: 
            segment.goto(1000, 1000)
        segments1.clear()
        score1 = 0
        delay = 0.08
        win.onkey(go_up1, "w")
        win.onkey(go_down1, "s")
        win.onkey(go_right1, "d")
        win.onkey(go_left1, "a")
        pen1.clear()
        pen1.write("P1 Score : {}  High Score : {}".format(score1,high_score1),align = "center",font = ("Courier",24,"normal"))
        
    if snakehead2.xcor() > 290 or snakehead2.xcor() < -290 or snakehead2.ycor() > 290 or snakehead2.ycor() < -290:
        time.sleep(0.1)
        snakehead2.goto(25, 100)
        snakehead2.direction = "stop" 
        for segment2 in segments2: 
            segment2.goto(1000, 1000)
        segments2.clear()
        score2 = 0
        delay = 0.08
        win.onkey(go_up2, "i")
        win.onkey(go_down2, "k")
        win.onkey(go_right2, "l")
        win.onkey(go_left2, "j")
        pen2.clear()
        pen2.write("P2 Score : {}  High Score : {}".format(score2,high_score2),align = "center",font = ("Courier",24,"normal"))
    
    movement1()
    
    movement2()
    
    for segment1 in segments1:
        if segment1.distance(snakehead1) < 20:
            time.sleep(0.1)
            snakehead1.goto(-25, 100)
            snakehead1.direction = "stop"
            for segment1 in segments1:
                segment1.goto(1000, 1000)
            segments1.clear()
            score1 = 0
            delay = 0.08
            win.onkey(go_up1, "w")
            win.onkey(go_down1, "s")
            win.onkey(go_right1, "d")
            win.onkey(go_left1, "a")
            pen1.clear()
            pen1.write("P1 Score : {}  High Score : {}".format(score1,high_score1),align = "center",font = ("Courier",24,"normal"))
            
    for segment2 in segments2:
        if segment2.distance(snakehead2) < 20:
            time.sleep(0.1)
            snakehead2.goto(25, 100)
            snakehead2.direction = "stop"
            for segment2 in segments2:
                segment2.goto(1000, 1000)
            segments2.clear()
            score2 = 0
            delay = 0.08
            win.onkey(go_up2, "i")
            win.onkey(go_down2, "k")
            win.onkey(go_right2, "l")
            win.onkey(go_left2, "j")
            pen2.clear()
            pen2.write("P2 Score : {}  High Score : {}".format(score2,high_score2),align = "center",font = ("Courier",24,"normal"))        
    
    time.sleep(delay)
    
    if snakehead1.distance(snakehead2)<15:
            snakehead1.goto(-25,100)
            snakehead2.goto(25,100)
            snakehead1.direction = "stop"
            snakehead2.direction = "stop"
            end.write("Game Over",align = "center",font = ("Courier",30,"normal"))
            if high_score1==high_score2:
                result.write("Tie",align = "center",font = ("Courier",30,"normal"))
            elif high_score2>high_score1:
                result.write("Player 2 wins",align = "center",font = ("Courier",30,"normal"))
            elif high_score1>high_score2:
                result.write("Player 1 wins",align = "center",font = ("Courier",30,"normal"))   
            break
win.mainloop()
turtle.done()