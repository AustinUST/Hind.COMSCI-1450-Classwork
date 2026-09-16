'''#question 1
count = 1
while (count <= 10):
    print(count)
    count += 1
#question 2
even = 2
while (even <=20) and (even % 2 == 0):
    print(even)
    even += 2
#Q3
num1 = int(input("Enter a number: "))
while (num1 >= 0):
    print(num1)
    num1 -= 1
#Q 4
num2 = 2
while (num2 <= 30):
    print(f"{num2} {num2 * num2}")
    num2 += 2
#Q5
Password = str(input("Enter the password: "))
Correct = "humpty"
while (Password != Correct):
    print("Invalid")
    Password = input("Try again: ")

#6
hu = int(23)
secret = int(input("Enter a number between 1 and 100: "))

while (secret != hu):
   print("too low")
   secret = int(input("Try again: "))
   if (secret < hu):
    print("Too low")
   elif (secret > hu):
    print("too high")
   else: 
     print("Correct")

#7
word = str(input("Enter a word: "))
while (word != "Stop"):
    print("Nah")
    word = input("Enter a word: ")
#8
n = int(input("Enter a positive integer: "))
total = 0
count = 1
while count <= n:
    total += count
    count += 1
print(f"The sum of all numbers from 1 to {n} is: {total}")
#9
num7 = 0
num9 = int(input("Enter a number (0 to stop): "))
while num9 != 0:
    num7 += num9
    num9 = int(input("Enter a number (0 to stop): "))

print(f"The total is: {num7}")
#10
Positive = 0
negative = 0

count = int(input("Enter a number negative or positive (Zero = stop): "))
while (count != 0):
    if (count > 0):
        Positive += 1
    else:
        negative += 1
    count = int(input("Enter a number negative or positive (Zero = Stop): "))
print(f"The number of positive numbers is {Positive}.")
print(F"The number of negative numbers is {negative}.")
#11
grade_count = 0 
total_grade = 0

while (grade_count < 6):
    student = float(input("Enter the grade for the student: "))
    total_grade += student
    grade_count += 1
average_grade = total_grade / 6
print(f"The average grade of the students is: {average_grade}.")
#12
pos_even = 0

number1 = int(input("Enter a number (Zero to stop): "))
while (number1 != 0):
    if (number1 > 0 and number1 % 2 == 0):
        if number1 > pos_even:
            pos_even = number1
    number1 = int(input("Enter another number (Zero to stop): "))
print(f"The largest even number is: {pos_even}. ")
#13
factor = 0
numb = int(input("Enter one number: "))
if (numb <= 0):
    print("Positive number expected")
else:
    factor = 1
    tot = 1
    while (tot <= numb):
        factor *= tot
        tot += 1
print(f"{numb}! = {factor}")
#14
for i in range (1,11):
    print(i)
#15
word = str(input("Enter your favorite word: "))
for i in range(5):
    print(word)
#16
for i in range(1,21):
    if(i % 2 == 0):
        print(i)
#17
nope = 0
user = int(input("Enter a number: "))
for i in range(1, user + 1):
    nope += i

print(f"The sum from 1 to {user} = {nope}. ")
#18
word1 = str(input("Enter a word: "))
a_count = 0
for letter in word1:
    if letter == "a":
        a_count += 1
print(f" The amount of times 'a' appears in the word is {a_count}")
'''
#19
for i in range(4):
    for j in range(4):
        print(i, end ="",) 
    print()
#20
for i in range(4):
    star = "*"
    for j in range(5):
        print(star, end="")
    print()
#21
for i in range(6):
    for j in range(i):
        print(j, end = "")
    print()
#22
for i in range(5):
    star1 = "*"
    for j in range(i):
        star1 += "*"
    print(star1)

