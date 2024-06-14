#https://github.com/ONETAPL3G3ND
class Test1:
    def __init__(self, name):
        self.name = name

class Test2(Test1):
    def __init__(self, version, name):
        self.version = version
        super().__init__(name)

class Test3(Test2):
    def __init__(self, time, version, name):
        self.time = time
        super().__init__(version, name)

if __name__ == "__main__":
    t = Test3("12:00", "1.0", "Vasya")
    print(vars(t))
