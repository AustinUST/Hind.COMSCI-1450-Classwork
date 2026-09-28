import math
import random
from random import randrange
from math import sqrt
#1
x1 = 3
x2 = 7
y1 = 5
y2 = 8
distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(distance)

#2 

angle = float(input("Input the angle above the horizontal: "))
radians = angle * (3.14 / 180)
sine = math.sin(radians)
cosine = math.cos(radians)

print(f"The radians of your value are,{radians}\nThe sine ={sine}\nThe cosine ={cosine}")

#3
rannum = random.uniform(0, 1)
print(rannum)
val = randrange(1,7)
print(val)
ab = "ABCDEFG"
letter = random.choice(ab)
print(letter)
count = 0
steps = randrange(10,51)
for i in range(steps):
    print(random.randrange(10,51))
    count += 1
    if (count == 10):
        break
    else:
        pass
#4
def show_welcome_banner():
    print("******************************")
    print("Welcome to Python Programming!")
    print("******************************")
show_welcome_banner()
#5
username = input("Enter your username: ")
def greet_user(username):
    print(f"Welcome back, {username}!")
print(greet_user(username))
#6
def even_or_odd(x):
    if (x % 2 ==0):
        print("even")
    elif (x % 2 != 0):
        print("Odd")
    return x
print(even_or_odd(10))
#7
def dollars_2_euros(x):
    dollar = float(input("Enter your USD: $"))
    euro_total = dollar * .92
    return euro_total
print(dollars_2_euros(0))
#8
def calculate_shipping(package_weight, distance_miles):
    package_weight = float(package_weight)
    distance_miles = float(distance_miles)

    if package_weight < 0 or distance_miles < 0:
        raise ValueError("Package weight and distance must be non-negative.")

    return package_weight * 0.5 + distance_miles * 0.1


weight = float(input("Enter the weight: "))
distance = float(input("Enter the distance in miles: "))
print(calculate_shipping(weight, distance))
#9
def vowels(y):
    """Return the number of vowels in the supplied text."""
    vowel_count = 0
    for character in y:
        if character.lower() in "aeiou":
            vowel_count += 1
    return vowel_count
print(vowels("hey"))
    
#10
def get_rectangle(x,y):
    area = x * y
    return area
print(get_rectangle(10,20))
#11
def maximum(a,b):
    if a > b:
        print(f"{a} is greater")
    elif b > a:
        print(f"{b} is greater")
    return a,b
print(maximum(3,5))
#12
def is_even(n):
    num = int(input("enter a number: "))
    if (num % 2 == 0):
        print(True)
    else:
        print(False)
    return num
print(is_even(0))
#13
from math import pow
def circle_area(r):
    area1 = r * r * 3.14
    return area1
print(circle_area(5))
#14
from math import factorial
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)
print(factorial(5))
