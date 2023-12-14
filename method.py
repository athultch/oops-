
class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

# Create an instance of the Student class
a1 = Student(10, 20, 19)

# Call the avg method on the instance
print(a1.avg())
