class Cars:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def start(self):
        print(self.name , self.price ,self.color)

car1 = Cars("maruthi", 1000000, "red")
car2 = Cars("tata", 1200000, "blue")


car1.start()
car2.start()
