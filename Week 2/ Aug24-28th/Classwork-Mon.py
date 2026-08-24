
num1 = 10 * 20
print(f"The number is {num1}")

if num1 > 100:
    print(f"{num1} is greater than 100")
else:
    print(f"{num1} is not greater than 100")


print("This is " + str(num1) + " it is small")

x = 5
y = float(x)
print(y)

# christmas tree attempt in binary
for r in range(3):
    star1 = "              *"
    for s in range(3):
        star1 += "*"
    print(star1)

for i in range(x):
    row1 = "               1"
    for j in range(5):
        row1 += "0"
        for k in range(j):
            row1 += "1"
        print(row1)


for h in range(6):
    row2 = "              0"
    for l in range(5, 7):
        row2 += "0"
        print(row2)


jump1 = 6.64674646

print(round(jump1, 3))
print("welcome to the world\nThe year is 2026 \"UST\".")



print('This is "UST"')
Name = str(input("enter your name: "))
print(f"Welcome to the class, {Name}!")


