############### windows
# from turtle import *
# speed(1)
# bgcolor('black')
# penup()
# goto(-50,60)
# pendown()
# color('cyan')
# begin_fill()
# goto(100,100)
# goto(100,-100)
# goto(-50,-60)
# goto(-50,60)
# end_fill()
# penup()
#
# color('black')
#
# goto(10,100)
# pendown()
# color('black')
# width(10)
# goto(10,-100)
# penup()
# goto(100,0)
# pendown()
# goto(-100,0)
#
# done()
################################  corona
# from turtle import *
# color('red')
# bgcolor('grey')
# speed(0)
# b=0
# while b<200:
#     right(b)
#     forward(b*3)
#     b = b + 1
# hideturtle()
# done
# ########################    sun
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# bgcolor('black')
# speed(0)
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
#####################################  rings
# import turtle as t
# Color=['orange','yellow','blue','green','violet','maroon','#00adef','dark salmon']
# t.speed(0)
# t.width(1)
#
#
# for color in Color:
#     t.fillcolor(color)
#     t.begin_fill()
#     t.circle(145)
#     t.circle(130,-360)
#     t.circle(115)
#     t.circle(100,-360)
#     t.end_fill()
#     t.right(45)
#
# t.hideturtle()
# t.done
####################################################       indian flag
from turtle import *
speed(0)
bgcolor('black')
penup()
color('orange')
begin_fill()
goto(-200,200)  #1st corner
pendown()
goto(200,200)   #2nd corner
goto(200,100)    #3rd corner
goto(-200,100)   #4th corner
goto(-200,200)  #1st corner
end_fill()

penup()
color('white')
begin_fill()
goto(-200,100)   #1st corner
pendown()
goto(200,100)    #2nd corner
goto(200,0)     #3rd corner
goto(-200,0)    #4th corner
goto(-200,100)
end_fill()

penup()
color('dark green')
goto(-200,0)
begin_fill()
pendown()
goto(200,0)
goto(200,-100)
goto(-200,-100)
end_fill()

penup()
color('blue4')
width(2)
goto(0,0)
begin_fill()
pendown()
circle(50)

penup()
goto(0,50)
pendown()
width(1)
color('blue4')
for i in range(24):
    forward(50)
    back(50)
    right(15)
hideturtle()
done()
#################################################


