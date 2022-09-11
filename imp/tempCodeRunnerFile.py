rt *
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


