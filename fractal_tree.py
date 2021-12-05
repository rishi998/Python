import turtle
tree=turtle.Turtle()
sc=turtle.Screen()
sc.bgcolor("black")
tree.speed(0)
tree.color("green")
tree.shape("turtle")
tree.lt(90)  #turtle facing up
tree.bk(100)  #turtle is placed at the starting position

def fruit(radius=2):   #function r=that will be called when a fruit is to be drawn on branches
    tree.circle(radius)

def Tree(i):   #defining a function that will take an argument i on which the size of the tree will depend.
    if i<10:   #base condition to return
        return
    else:
        tree.fd(i)   #the lowest stem of tree will be drawn 
        tree.color("orange")     #changing the color of the turtle to ensure the fruit color is always orange.
        fruit()     #calling the fruit function
        tree.color("brown")    #changing the color again for branches.
        tree.lt(30)    #turtle will move 30 degrees left always a branch is made to ensure the tree is enlarging.
        Tree(3*i/4)    #the tree function is called again with i=75. initially it was i=100.
        tree.rt(60)    #whenever i will reach less than 10 the control will be returned to this line segment(to start drawing branches from right direction).
        Tree(3*i/4)    #when turtle turned 60 degrees right , it needs to continue drawing branches.
        tree.lt(30)    
        tree.bk(i)    #get back to the original position
Tree(100)

turtle.mainloop()