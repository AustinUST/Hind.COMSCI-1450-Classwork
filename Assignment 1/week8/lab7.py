#1
o = [2,3,4,5,6]
for i in o:
    print(i)
#2
print(o[0],o[4])
#3
if o[2] == 4:
    print(True)
else:
    print(False)
#4
sum = 0
for m in o:
    sum += m
print(sum)
#5
for n in o:
    avg = sum / len(o)
print(avg)
#6
largest = o[0]
for x in o:
    if x > largest:
        largest = x
print(largest)
#7
smallest = o[0]
for y in o:
    if y < smallest:
        smallest = y
print(smallest)
#8
list1 = [1,2,3,4,3,4,6,2,5,6,8,10,22,74,504]
print(list1)

square = [x ** 2 for x in list1]
print(square)
even = [x for x in list1 if x % 2 == 0]
print(even)
odd = [x for x in list1 if x % 2 != 0]
print(odd)
cubed = [x ** 3 for x in list1]
print(cubed)
 
eve = 0
od = 0
for z in list1:
    if z % 2 == 0:
        eve += 1
    else:
        od += 1
print("The number of even numbers in the list is:", eve)
print("The number of odd numbers in the list is:", od)

x = []
for i in list1:
    if i not in x:
        x.append(i)
print(x)

list2 = [-100, -1, 2, 4, 5, 6, -7, 3, -2, 0]

merge = [list1 + list2]
print(merge)
def merge_lists(list1, list2):
    merged_list = list1 + list2
    return merged_list
print(merge_lists(list1, list2))

list1.extend(list2)
print(list1)

pos =[x for x in list1 if x > 0]
print(f"The positive numbers in the list are: {pos}")
neg = [x for x in list1 if x < 0]
print(f"The negative numbers in the list are: {neg}")

word = ["python", "texas", "ust", "nevermind", "find me", "hello", "world", "whats up"]
four = [x for x in word if len(x) > 4]
count4 = len(four)
print(f"The words with 4 letters in the list are: {four}, count: {count4}")

squared = [x ** 2  for x in list1]
print(f"The squares of the merged list are: {squared}")

yup = tuple(list1)
if 20 in yup:
    print("True")
else:
    print("False")