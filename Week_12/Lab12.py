#1
class Animal:
    def __init__(self, name,):
        self.name = name
    def eat(self):
        return f"{self.name} is eating."
class cat(Animal):
     def meow(self):
         print(f"{self.name} says Meow!")
c1 = cat("Whiskers")
c1.meow()
c1.eat()
#2
class shape:
    def __init__(self, describe, name):
        self.name = name
        self.describe = describe
    def sides(self):
        return f"{self.name} has {self.describe} sides."
class square(shape):
    def __init__(self, describe, name):
        super().__init__(describe, name)
    def area(self, side_length):
        return f"The area of {self.name} is {side_length ** 2}."
s1 = square(4, "Square")
print(s1.sides())
print(s1.area(5))
#4
class manager:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    def manage(self):
        return f"{self.name} manages the {self.department} department."
class employee(manager):
    def __init__(self, name, department, position):
        super().__init__(name, department)
        self.position = position
    def work(self):
        return f"{self.name} works as a {self.position} in the {self.department} department."
e1 = employee("Alice", "HR", "Recruiter")
print(e1.manage())
print(e1.work())
#5


