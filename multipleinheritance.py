class A:
    def feature1(self):
        print("feature1 working")

class B:
    def feature2(self):
        print("feature2 working")

class C(A,B):
    def feature3(self):
        print("feature3 working")

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()