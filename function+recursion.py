# def greet(name="Everyone"): # everyone is a default perimeter
#     gr=print("Good Night", name)
#     return gr

# greet("Rishi")
# greet()

#recursion in calculating factorial
# def fact_recursive(n):
#     if n==1 or n==0:
#        return 1
#     return n * fact_recursive(n-1)

# print(fact_recursive(10))

#program for greatest of three numbers
# def func(a,b,c):
#     if a>b:
#         if a>c:
#             print(a, " is greatest")
#         else:
#             print(c," is greatest")
#     else:
#         if b>c:
#             print(b, " is greatest")
#         else:
#             print(c, " is greatest")
# a=int(input("Enter 1st number"))
# b=int(input("Enter 2nd number"))
# c=int(input("Enter 3rd number"))
# func(a,b,c)

#program to convert degree celcius to fahrenheit
# def fahr(x):
#     return x*(9/5) + 32

# celc=float(input("Enter temp in degree celcius: "))
# temp=fahr(celc)
# print(temp, " is the temperature in degrees fahrenheit")

#recursion program to find the sum of first n natural numbers
# def sum(n):
#     if n<=0:
#         return n
#     return n + sum(n-1)
# num=int(input("Enter a natural number: "))
# print(sum(num))

#printing star pattern using recursion
# def print_pattern(n):
#     if n<=0:
#        return print("Add atleast a single line")
#     return print(" * "*n),print_pattern(n-1) 
# rows=int(input("Enter the number of rows: "))
# print_pattern(rows)

#recursion program to demonstrate strip and remove functions of strings
# def remove_and_split(string, word):
#     newstr=string.replace(word, "")
#     return newstr.strip()
# this="Rishi is a good boy           "
# n=remove_and_split(this, "Rishi")
# print(n)

#multiplication table using recursion
# def table(n,i):
#     if i>10:
#         return n
#     print(f"{n}X{i}={n*i}")
#     return table(n,i+1)

# num=int(input("Enter n and i: "))
# i=1
# table(num,i)

#program to sum all elements of a list
# def sum(nums):
#     Sum=0
#     for i in nums:
#        Sum+=i
#     return Sum
# print(sum((2,4,6,8,10)))
#program to multiply all elements of a list
# def multiply(nums):
#     prod=1
#     for i in nums:
#         prod*=i
#     return prod
# print(multiply((1,2,3,4,5,6)))

#program to reverse a string
# str=input("Enter a string: ")
# def rev_string(a):
#     rstr=''
#     length=len(a)
#     while length>0:
#         rstr+=a[length-1]
#         length-=1
#     return rstr
# print(rev_string(str))

#recursion
# def do_n(a,n):
#     if n==0:
#         print("blastoff!!")
#     elif n<0:
#         return
#     else:
#         print(a)
#     do_n(a,n-1)
# a="hello"
# n=int(input("Enter a number: "))
# do_n(a,n)

# import time
# epoch=time.time()
# seconds_in_a_day=24*60*60
# seconds_in_an_hour=60*60
# seconds_in_a_minute=60
# days=epoch//seconds_in_a_day
# hours=(epoch%seconds_in_a_day)//seconds_in_an_hour//seconds_in_a_minute+8
# minutes=(epoch%seconds_in_a_day)%seconds_in_an_hour//seconds_in_a_minute
# seconds=(epoch%seconds_in_a_day)%seconds_in_an_hour%seconds_in_a_minute
# print("%s: %s: %s: %s" %(days,hours,minutes,seconds))
# print("New Delhi Current time is %d: %d: %d: %d" %2(days, hours, minutes, seconds))

#fermat's theorem
# def check_fermat(a,b,c,n):
#     if n<=2 or n>=0:
#         print("No! that doesn't work!!")
#     else:
#         if a**n + b**n ==c**n:
#             print("Holy smokes!!, Fermat was wrong!!")
#         else:
#             print("No! that doesn't work!!")
#     # check_fermat(a,b,c,n-1)
# a=int(input("Enter a: "))
# b=int(input("Enter a: "))
# c=int(input("Enter a: "))
# n=int(input("Enter power: "))
# check_fermat(a,b,c,n)

#triangle
# def is_triangle(a,b,c):
#     d="YES!!"
#     e="No!!"
#     if a+b<c or a+c<b or b+c<a:
#         print("Can a triagle be formed with these lengths??,",e)
#     elif a+b==c or a+c==b or b+c==a :
#         print("Degenerate triangle!")
#     else:
#         print("Can a triagle be formed with these lengths??,",d)
# a=int(input("Enter length of first side of a triangle: "))
# b=int(input("Enter length of second side of a triangle: "))
# c=int(input("Enter length of third side of a triangle: "))
# is_triangle(a,b,c)

# def recurse(n,s):
#     if n==0:
#         print(s)
#     else:
#         recurse(n-1,n+s)
# recurse(-1,0)

#lambda function
# def myfunc(n):
#     return lambda a: a*n
# double=myfunc(2,3)
# print(double)

# class employee:
#     def __init__(self, age, name):
#         self.name=name
#         self.age=age
# p1=employee("ravi",24)
# print(p1.name)
# print(p1.age)

class greet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def muf(self):
        print('Hello my name is '+ self.name)
p1=greet("rishi",20)
p1.muf()