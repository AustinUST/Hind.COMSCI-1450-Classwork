'''A university evaluates applicants using the following rules:
An applicant is accepted if:
● GPA is at least 3.0 and SAT score is at least 1100, or
● GPA is at least 3.5 and SAT score is at least 1000.
However, an applicant must have a GPA of at least 2.5 to be considered.
Write a Python program that asks for the student's GPA and SAT score and
prints:
● "Accepted"
● "Rejected"
● "Invalid GPA" if GPA is outside 0.0–4.0
● "Invalid SAT score" if the SAT score is negative
2. Write a program that calculates shipping costs based on the package
weight and whether the customer has a premium membership.
Rules:
● Weight ≤ 2 kg → $5
● Weight > 2 kg and ≤ 5 kg → $10
● Weight > 5 kg and ≤ 10 kg → $15
● Weight > 10 kg → $25
Premium members receive free shipping if the package weighs 5 kg or less.
The program should reject zero or negative weights.'''

gpa = float(input("Enter your GPA on a 4.0 scale: "))
sat = int(input("Enter your SAT Score: "))
if (gpa >= 3.5) and (sat >= 1000):
    print("Accepted")
elif (gpa >= 3.0) and (sat >= 1100):
    print("Accepted")
else:
    print("Rejected")
if (gpa < 0.0) or (gpa >4.0):
    print("Invalid GPA")
elif (sat < 0):
    print("Invalid SAT score")
else: 
    pass

package_weight = float(input("Enter the package weight in kg: "))
premium_member = str(input("Are you a premium member? (yes/no): "))
if (package_weight <= 2):
    if (premium_member == "yes" and package_weight <= 5):
        print("Shipping cost: free")
    else:
        print("Shipping cost: $5")
elif (package_weight <= 5):
    if (premium_member == "yes" and package_weight <= 5):
        print("Shipping cost: free")
    else:
         print("Shipping cost: $10")
elif (package_weight <= 10):
    print("Shipping cost: $15")
else:
    print("Shipping cost: $25")
if (package_weight <= 0):
    print("Invalid weight")
else:
    pass
