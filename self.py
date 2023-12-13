class CV:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Taking input from the user
name1= input("Enter name: ")
age1= int(input("Enter age: "))

name2= input("Enter name: ")
age2= int(input("Enter age: "))


# Creating an instance of the CV class with user input
person1 = CV(name1, age1)
person2 = CV(name2, age2)


 
# Checking access for each person
if person1.age >= 18:
    print(f"Access granted for {person1.name}!")
else:
    print(f"Access denied for {person1.name}.")

if person2.age >= 18:
    print(f"Access granted for {person2.name}!")
else:
    print(f"Access denied for {person2.name}.")