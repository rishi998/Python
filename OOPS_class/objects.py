class computer:
    def __init__(self,ram,cpu):
        self.ram=ram
        self.cpu=cpu

    monitor='samsung'
    def config(self):
        print("The specs of this compter is: ",self.ram,self.cpu,self.monitor)

    def compare(self,com2):
        if self.ram==com2.ram:
            return True
        else:
            return False 


com1=computer('4gb', 'i5')
com2=computer('6gb','i6')

com1.ram='10gb'

com1.config()
com2.config()

if com1.compare(com2):
    print("They are same!!")
else:
    print("They are different!!")
# com1.config()
     