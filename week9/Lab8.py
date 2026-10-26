#1
d = {'apples': 50, 'bananas': 30, 'oranges': 25}
d['bananas'] = 45
d['mangoes'] = 15

del d['oranges']
print(d)
#2
def gel_stock(d, item):
    return d.get(item, "Not in stock")
print(gel_stock(d,'non'))

#3
keys = {"Name": "Alex", "Age": 24, "Role": "Developer"}
print(keys)
#4
'''Write a Python program to print the key and value of items where
the values are greater than 50 in a dictionary'''

n = {"Number": 45, "Age": 80, "money": 90100}
for i in num:
    if i > 50:
        print(num)
