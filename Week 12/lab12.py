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

class price:
    def __init__(self, item, cost):
        self.item = item
        self.cost = cost
    def display_price(self):
        return f"The price of {self.item} is ${self.cost}."
class discount(price):
    def __init__(self, item, cost, discount_percentage):
        super().__init__(item, cost)
        self.discount_percentage = discount_percentage
    def discounted_price(self):
        discounted_cost = self.cost * (1 - self.discount_percentage / 100)
        return f"The discounted price of {self.item} is ${discounted_cost:.2f}."
d1 = discount("Laptop", 1000, 10)
print(d1.display_price())
print(d1.discounted_price())    