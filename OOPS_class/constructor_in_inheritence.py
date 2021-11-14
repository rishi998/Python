class A:
    def __init__(self):
        print("init a")

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")
    
class B(A):
    def __init__(self):
        super().__init__()
        print("init b")
    
    def feature3(self):
        print("afeaure 3 is working")

    def feature4(self):
        print("afeaure 4 is working")

c1=B()
    
    