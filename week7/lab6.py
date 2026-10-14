#1
'''
A security script requires text clean-up before processing
credentials. Write a function named
validate_access_code(raw_code) that accepts a single string
argument. Inside the function:
• Remove all accidental spaces from the beginning and end of the
string using a string method.
• Convert the entire code into absolute lowercase characters.
• Check the cleaned text string against two rules:
o It must strictly start with the prefix "admin".
o It must strictly end with the suffix "2026".
• If both rules are met, return True. Otherwise, return False.
• Prompt the user to enter a raw code string using input().
• Call validate_access_code(raw_code).
• Print a success message if it returns True, or an access denied
message if it returns False'''
from importlib.metadata import files

from sympy import together


'''def validate_access_code(raw_code):
    cleaned_code = raw_code.strip().lower()
    if cleaned_code.startswith("admin") and cleaned_code.endswith("2026"):
        return True
    else:
        return False
raw_code = input("Enter the raw code string: ")
if validate_access_code(raw_code):
    print("Access granted. Welcome!")
else:
    print("Access denied. Invalid code.")'''


#2

def audit_text_stream(flagged_word):
    occurrence_total = 0
    while True:
        sentence = input("Enter a sentence (or type 'exit' to quit): ")
        if sentence == "exit" or sentence == "Exit" or sentence == "EXIT":
            break
        cleaned_sentence = sentence.lower()
        occurrence_total += cleaned_sentence.count(flagged_word)
    return occurrence_total
#3

def verify_file_record(line_content):
    f = open("#3.txt", "w")
    f.write(line_content)
    f.close()

#4
f = open("Q4.txt", "w")
f.write("10")
f.write("\n20")
f.write("\n15")
f.write("\n25")
f.write("\n30")

f.close()

w = open("Q4.txt", "r")

sum = 0
for line in w:
    if int(line.strip()) % 2 == 0:
        sum += int(line.strip())
    else:
        pass
print("The sum of the numbers in the file is:", sum)
avg = sum / 3
print("The average of the numbers in the file is:", avg)
w.close()

#5
f = open("numbers.txt", "r")
sum = 0
for line in f:
    sum += int(line.strip())
print("The sum of the numbers in the file is:", sum)
f.close()
#6
x = []
total = 0
for i in range(5):
    num = int(input("Enter a number: "))
    x.append(num)
    total += num
print("The sum of the numbers is:", total)


