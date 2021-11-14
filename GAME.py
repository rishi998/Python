import random
def game(comp, you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
comp=print("Comp turn:: snake(s) Water(w) Gun(g)?")
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
else:
    randno=3
    comp='g'
you=input("Your turn:: snake(s) Water(w) Gun(g)? ")
a=game(comp,you)
print(f"\nComputer chose:{comp}")
print(f"You chose:{you}\n")
if a==None:
    print("Tie!!")
elif a==True:
    print("You Win!!")
else:
    print("You Lose")


