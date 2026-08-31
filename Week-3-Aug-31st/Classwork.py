second = 7800
hrs = second / 3600
print(hrs)
sec = second % 3600
print(sec)
minutes = sec // 60
print(minutes)

num1 = minutes % 2
if num1 == 0:
    print(f"{num1} is an even number" )
else:
    print(f"{num1} is an odd number")

num2 = bool(input("True or False, you are a male: "))
if num2 == False:
    print("You are not a male, you cannot enter the men's restroom")
else:
    print("You may enter")



