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
