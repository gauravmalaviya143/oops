class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("feature1-A working")

class B:
    def __init__(self):
        print("in B init")

    def feature1(self):
        print("feature1-B working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")

    def feature2(self):
        super().feature1()

c1 = C()
c1.feature1()
c1.feature2()
