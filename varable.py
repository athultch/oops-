class Car:
    def __init__(self):
        self.mil = 10
        self.name = "bmw"

    def __str__(self):
        return f"Car(name={self.name}, mileage={self.mil})"

# Create an instance of the Car class
c1 = Car()

# Print the instance using the __str__ method
print(c1)
