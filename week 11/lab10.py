import tkinter as tk

from numpy import negative    

'''
#1
while True:
    try:
        numerator = float(input("Enter a number: "))
        denominator = float(input("Enter a number: "))
        z = numerator / denominator
        print(f"The result of {numerator} divided by {denominator} is: {z}")
    except ValueError:
        print("Invalid input. Please enter numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    


list1 = ["Laptop", "headphones", "Backpack", "water bottle"]
index = (input("Enter an index to access the list: "))
try:
    print(f"The item at index {index} is: {list1[index]}")
except IndexError:
    print("Error: Index is out of bounds.")
except ValueError:
    print("Invalid input. Please enter a valid integer index.")
except Exception as e:
    print(f"An unexpected error occurred: {e}"

account_balance = 500
withdraw = float(input("Enter the amount to withdraw: "))
try:
    if withdraw <= 0:
        print("Withdrawal must be greater than $0")
    elif withdraw > account_balance:
        print("Insufficient funds for this withdrawal.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    account_balance -= withdraw
    print(f"Withdrawal successful. New account balance: ${account_balance:.2f}")
'''

try:
    file = open("grade.txt", "r")
    al = file.read()
    add = al.splitlines()
    print(add)
except FileNotFoundError:
    print("Error: The file 'grade.txt' was not found.")
finally:
    file.close()
    