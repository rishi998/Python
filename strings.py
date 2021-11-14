# name="rishi Mehto is a good boy with all qualitites and in every aspect of life he is perfect."
# print(name[0:8])#prints 8 characters strating from index zero.
# print(name[0:11])
# print(name[0:])#same as name[0:11]
# print(name[:5])#same as name[0:5]
# print(name[0::2])#prints every 2nd character only.

# #string functions
# print(len(name))
# print(name.replace("is" , "iz"))
# print(name.capitalize())
# print(name.endswith("perfect."))
# print(name.count("i"))
# print(name.find("is"))

#practice set
# print("Enter your name: ")

# a=input()
# print("Good Afternoon,",a)

name=input()
date=input()
letter='''Dear <|Name|>
You are selected!!
Date <|Date|>'''
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)
