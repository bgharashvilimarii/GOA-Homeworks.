from turtle import *

#we want to print a house

#step 1 draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90) 

forward(200)
left(90)

forward(200)
left(90)
 
#end of square
 
#drawing a door
 

forward(70)
begin_fill()
color("yellow")
left(90) 
forward(120)
right(90)      
forward(60)
right(90)
forward(120)
end_fill()

#end of door




penup()
goto(200, 200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()  
#end of triangle
  

penup()
goto(200, 180)
pendown()

color("brown")
begin_fill()
right(60)
forward(50)
left(90)
forward(60)
left(90)
forward(50)
end_fill()

penup()
goto(0,180)
pendown()

color("brown")
begin_fill()
forward(50)
right(90)
forward(60)
right(90)
forward(50)
end_fill()



exitonclick()


