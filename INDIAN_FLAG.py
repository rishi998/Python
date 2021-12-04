import turtle
flag = turtle.Turtle()
flag.speed(10)
flag.pensize(2)

# TODO:
# 1. Let argument names be informative. Eg. radius instead of 'r'

def draw_ashok_chakra(radius):
    flag.color("blue")
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

#   ------------------------------------------
#   |                                        |
#   |                                        |
#   --------------------->--------------------
#  T - Turtle location
#  default angle - 0 degrees (>)
# TODO:
# 1. Do not take angle as argument since rectangles are always 90 degrees
# 2. Rename c arg to fill_color=None

# TODO:
# 0. Rectangles should start from one direction only
# 1. A black colored boundary around the whole flag
# 2. Draw a flag pole on the left
# 3. White rectangle should be same width as the others
# 4. Handle "small" and "large" as arguments for size of the flag

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


def draw_small_flag(size="small"):
#moving the turtle initial position to 100 units upwards
    flag.lt(90)
    lookup(100)
    flag.rt(90)
#now initialy turtle is facing towards right
    draw_ashok_chakra(20)
    flag.rt(90)
    lookup(15)
    flag.lt(90)
    draw_rectangles(400, 70, "green")
    flag.lt(90)
    lookup(140)
    flag.rt(90)
    draw_rectangles(400, 70, "orange")
    flag.lt(90)
    lookup(15)
#drawing the borders of the flag
    draw_border(430,240)
    draw_pole(10,900,225,"brown",12)



def draw_medium_flag(size="medium"):
    flag.lt(90)
    lookup(100)
    flag.rt(90)
    draw_ashok_chakra(30)
    flag.rt(90)
    lookup(20)
    flag.lt(90)
    draw_rectangles(600, 100, "green")
    flag.lt(90)
    lookup(200)
    flag.rt(90)
    draw_rectangles(600, 100, "orange")
    flag.lt(90)
    lookup(15)
    draw_border(630,330)
    draw_pole(15,900,325,"brown",16)


def draw_large_flag(size="large"):
    flag.lt(90)
    lookup(100)
    flag.rt(90)
    draw_ashok_chakra(40)
    flag.rt(90)
    lookup(25)
    flag.lt(90)
    draw_rectangles(800, 130, "green")
    flag.lt(90)
    lookup(260)
    flag.rt(90)
    draw_rectangles(800, 130, "orange")
    flag.lt(90)
    lookup(15)
    draw_border(830,420)
    draw_pole(20,900,435,"brown",20)


choice=int(input("Enter the size of the flag. 1 for small, 2 for medium and 3 for large:  "))
if choice==1:
    draw_small_flag(size="small")
elif choice==2:
    draw_medium_flag(size="medium")
else:
    draw_large_flag(size="large")
turtle.mainloop()
