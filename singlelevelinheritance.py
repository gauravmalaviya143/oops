class A:
    def feature1(self):
        print("feature1 working")

class B(A):
    def feature2(self):
        print("feature2 working")

b1 = B()
b1.feature1()
b1.feature2()