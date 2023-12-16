class Laptop:
    def __init__(self):
        self.brand = 'HP'
        self.proce = 'i7'
        self.ram = 16

    def show(self):
        print(self.brand, self.proce, self.ram)


class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()


S1 = Student('athul', 5)
S2 = Student('vishnu', 9)

S2.show()
S1.show()



