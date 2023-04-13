import turtle
import colorsys
import time
t=turtle.Turtle()
time.sleep(2)
turtle.Screen().bgcolor('black')
t.pensize(2)
t.speed(0)
n=100
h=0
for i  in range(100):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n 
    t.color(c)
    t.left
    t.circle(i*1.2,180)
    t.circle(i,-180)
    t.circle(i,-60)
    for i in range(4):
        t.circle(40+i*5,-90)
        t.forward(200)
        t.right(90)
    t.left(10)
turtle.done()