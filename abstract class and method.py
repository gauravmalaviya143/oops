from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(computer):
    def process(self):
        print("it's running")

class programmer:
    def work(self):
        print("solving bugs")

com1 = Laptop()
com1.process()
prog1 =programmer()
prog1.work()
