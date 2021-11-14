#program to add two numbers
# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# sum=a+b
# print(sum)

#program to greatest of two numbers
# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# if a>b:
#     print(a, " is greater")
# else: 
#     print(b," is greater")

#factorial of a number
# def fact(num):
#     if num==1 or num==0:
#         return 1
#     else:
#        return num*fact(num-1)
# num=int(input("Enter a number: "))
# print(fact(num))

#compund interst
# p=int(input("Enter the principal amount:"))
# r=int(input("Enter the rate of interst: "))
# n=int(input("Enter the times interst applied per time period: "))
# t=int(input("Enter the number of years: "))
# (A)=p(1+r/n)**(n*t)
# print(A)

#armstrong number

x=1
y=10000
for i in range(x,y+1):    
    order=len(str(i))  
    res=0
    k=i
    while k>0:
        l=k%10
        res=res+l*l*l
        k=k//10
    if i==res:
        print(i)




