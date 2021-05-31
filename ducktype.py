class Pycharm:
    def execute(self):
        print("compiling")
        print("running")

class MyEditor:
    def execute(self):
        print("spell check")
        print("convetion check")
        print("compiling")
        print("running")

class Laptop:
    def code(self,ide):
        ide.execute()

ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)