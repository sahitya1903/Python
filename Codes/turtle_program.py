# import turtle as t
# a=t.Turtle()
# a.left(90)
# a.forward(-100)
# a.left(90)
# a.forward(-100)
# a.left(90)
# a.forward(-100)
# a.left(90)
# t.done()
# a.forward(200)
# a.right(120)
# a.forward(200)
# a.right(120)
# a.forward(200)
# a.right(120)

# for i in range(50,0,-1):
#     a.forward(i-20)
#     a.left(90)

# s=t.Screen()
# s.bgcolor('red')
# a.color('white')
# a.speed(50)
# for i in range(200,21,-5):
#     a.circle(i-20)
# a.up()
# a.goto(300,300)
# a.down()
# for i in range(50,0,-1):
#     a.forward(i-10)
#     a.left(90)
# a.hideturtle()
# t.done()

# t.penup()
# t.circle(100)
# t.done()

# s=t.Screen()
# s.bgcolor('red')
# a.color('white')
# x=int(input('Enter number of shapes you want to draw:'))
# for i in range(x):
#     a.down()
#     n=int(input('Enter number of sides:'))
#     l=int(input('Enter length of side less than 200 units:'))
#     angle=360/n
#     for i in range(n):
#         a.forward(l)
#         a.right(angle)
#     a.up()
#     a.forward(200)

# a.fillcolor('green')
# t.done()

# for i in range(3):
#     a.forward(100)
#     a.left(120)


# for i in range(4):
#     a.forward(100)
#     a.left(90)
# t.done()
# import turtle as t
# a=t.Turtle()
# for i in range(2):
#     a.forward(100)
#     a.left(90)
#     a.forward(75)
#     a.left(90)
# t.done()



# for i in range(84,0,-6):
#     a.forward(i)
#     a.left(90)
#     a.forward(i)
#     a.left(90)
# a.up()
# a.goto(500,500)
# a.down()
# for i in range(84,0,-6):
#     a.circle(i)
#     a.up()
#     a.goto(i+100,i+100)
#     a.down()

# for i in range(84,0,-6):
#     a.circle(i,180)


# a.circle(100,steps=5)
import turtle 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Turtle() 
turtle.bgcolor('black')
t.speed(100)
for x in range(360): 
    t.pencolor(colors[x%6]) 
    t.width(x//100 + 1) 
    t.forward(x) 
    t.left(59)
turtle.done()