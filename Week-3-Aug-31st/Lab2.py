num1 = int(input("enter a number: "))
#Positive or negative
if(num1 <= 0):
    print(f"{num1} is negative")
else:
    print(f"{num1} is positive")
#Even or odd
if(num1 % 2 == 0):
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")
#Age check
age = int(input("Enter your age: "))
if(age >= 19):
    print("Teenager")
else:
    print("Adult")
#Temp check
temp = float(input("Enter the temperature: "))
if(temp <= 80):
    print("It is cold oustide")
else:
    print("It is hot outside")
#Greater or less than
num3 = int(input("Enter number 1: "))
num4 = int(input("Enter number 2: "))
if(num3 > num4):
    print("Number 1 is greater than Number 2")
else:
    print("Number 2 is greater than Number 1")
#Inside the range
score = int(input("Enter your score: "))
if(score >= 1 and score <= 100):
    print("Good score")
else:
    print("!Invalid Score!")
#Equal or not
num7 = int(input("Enter a number: "))
num8 = int(input("Enter a second number: "))
if(num7 == num8):
    print("same")
else:
    print("not same")
#pin check
pin = int(input("Enter your pin: "))
if(pin == 1234):
    print("Access granted")
else: 
    print("Access denied")
#Temperature check using elif
temp6 = float(input("Enter the temperature: "))
if(temp6 > 100):
    print("It is very hot outside")
elif(temp6 <= 100 and temp6 >= 80):
    print("It is hot outside")
elif(temp6 <= 79 and temp6 >= 60):
    print("It is warm outside")
else:
    print("It is cold outside")
#Grade check using elif
grade = int(input("Enter your grade: "))
if(grade >= 90):
    print("A")
elif(grade >= 80 and grade < 90):
    print("B")
elif(grade >= 70 and grade < 80):
    print("C")
elif(grade >= 60 and grade < 70):
    print("D")
else:
    print("F")
#greatest number
bro1 = int(input("Enter a number: "))
bro2 = int(input("Enter a second number: "))
bro3 = int(input("Enter a third number: "))
if(bro1 > bro2 and bro1 > bro3):
    print(f"{bro1} is the greatest number")
elif(bro2 > bro1 and bro2 > bro3):
    print(f"{bro2} is the greatest number")
else:
    print(f"{bro3} is the greatest number")
#Ticket cost
age1 = int(input("Enter your age: "))
if(age1 <= 13):
    print("Child, ticket is $5")
elif(age1 >= 14 and age1 <= 17):
    print("Teenager, ticket is $8")
elif(age1 >= 18 and age1 < 65):
    print("Adult ticket is $12")
else:
    print("Senior ticket is $7")
#Calculator
Calc = input("Enter what you want to calculate using (+, -, *, /): ")
num10 = float(input("Enter the first number: "))
num11 = float(input("Enter the second number: "))
if(Calc == '*'):
    product = num10 * num11
    print(f"{product}")
elif(Calc == '/'):
    if(num11 != 0):
        quotient = num10 / num11
        print(f"{quotient}")
    else:
        print("Error: Division by zero is not allowed.")
elif(Calc == '+'):
    sum = num10 + num11
    print(f"{sum}")
elif(Calc == '-'):
    difference = num10 - num11
    print(f"{difference}")