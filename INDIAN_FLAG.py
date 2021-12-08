
#   ------------------------------------------
#   |                                        |
#   |                                        |
#   --------------------->--------------------
#  T - Turtle location
#  default angle - 0 degrees (>)
# TODO:
# 1. Do not take angle as argument since rectangles are always 90 degrees
# 2. Rename c arg to fill_color=None

# TODO: Assignment 1
# 0. Rectangles should start from one direction only
# 1. A black colored boundary around the whole flag
# 2. Draw a flag pole on the left
# 3. White rectangle should be same width as the others
# 4. Handle "small" and "large" as arguments for size of the flag

# TODO: Assignment 2
# 1. Instead of separate functions: draw_small_flag(), draw_medium_flag().. etc.,
#    have only one function
#    Vary the length, breadth, radius etc. based on the flag size.
# 2. 100 = medium
#    70
#    150
#    130 
import turtle
import math
flag = turtle.Turtle()
flag.speed(10)
flag.pensize(2)
def draw_ashok_chakra(radius,size):
    flag.color("blue")
    count=0
    if size<100:
        for i in range(24):
           flag.fd(radius)
           flag.bk(radius)
           flag.lt(15*100/size)
           count+=1
           if count>size*24/100:
              break
    else:
        for i in range(24):
           flag.fd(radius)
           flag.bk(radius)
           flag.lt(15)
    flag.rt(90)
    flag.fd(radius)
    flag.lt(90)
    flag.circle(radius)

def lookup(distance):
    flag.penup()
    flag.fd(distance)
    flag.pendown()

def draw_rectangles(length, breadth, color=None):
    flag.color(color)
    flag.begin_fill()
    draw_border_lines(length,breadth)
    flag.end_fill()

def draw_border_lines(length,breadth):
    flag.fd(length/2)
    flag.rt(90)
    flag.fd(breadth)
    flag.rt(90)
    flag.fd(length)
    flag.rt(90)
    flag.fd(breadth)
    flag.rt(90)
    flag.fd(length/2)

def draw_border(length,breadth):
    flag.rt(90)
    flag.color("black")
    flag.pensize(1) 
    draw_border_lines(length,breadth)

def draw_pole(length,breadth,distance,color,radius):
    flag.lt(180)
    lookup(distance)
    flag.rt(90)
    lookup(10)
    flag.rt(90)
    flag.color(color)
    flag.begin_fill()
    flag.circle(radius)
    flag.end_fill()
    draw_rectangles(length,breadth,"grey")

# class Sizes():
#     radius: int
#     distance: int
#     length: int
#     breadth: int
#     color: str
# small_size = Sizes(20, 15, 400, 70)
# medium_size = Sizes(30, 20, 600, 100)
# large_size = Sizes(40, 25, 800, 130)

def draw_flag(size=100):
    # sizes = {"small": small_size,
    #          "medium": medium_size,
    #          "large": large_size}
    # current_size = sizes[size]

    flag.lt(90)
    lookup(100*size/100)
    flag.rt(90)
    draw_ashok_chakra(30*size/100,size)
    flag.rt(90)
    lookup(20*size/100)
    flag.lt(90)
    draw_rectangles(600*size/100,100*size/100, "green")
    flag.lt(90)
    lookup(200*size/100)
    flag.rt(90)
    draw_rectangles(600*size/100, 100*size/100, "orange")
    flag.lt(90)
    lookup(15*size/100)
    draw_border(630*size/100,330*size/100)
    draw_pole(15*size/100,900*size/100,325*size/100,"brown",16*size/100)

size=float(input("Enter the size of the flag"))
draw_flag(size)
flag.hideturtle()
turtle.mainloop()
