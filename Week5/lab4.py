word = "hahahahhahaahahahah"
a = 0
o = 0
for i in word: 
    if (i == "a"):
        a += 1
print(f"The count of 'A' is {a}")   

for letter in word:
    if (letter == "h"):
        o += 1

print(f"The count of 'O' is {o}")
