'''Receipt Generator & Currency Conversion
You will create a simple Python program for an international retail shop.
Assignment Requirements
Create one Python script file that follows the requirements below in the exact order.

Part 1 — Information Ingestion
Your program must ask the user for the following information:
The customer's name using the prompt: What is your name?
The number of items purchased using the prompt: Enter the number of items:
The price per item in USD using the prompt: Enter the price per item in USD:

Make sure you use input() and convert numerical inputs to the appropriate data type.

Part 2 — Data Processing
Your program must:
Calculate the USD subtotal: quantity × unit cost
Use the following exchange rate: 1 USD = 0.92 EUR
Calculate the total cost in Euros.
Use Python's built-in round() function to round the Euro total to exactly 2 decimal places.

Part 3 — Receipt Output

Your program should display the information in a format similar to the example below.

What is your name? Alice
Enter the number of items: 4
Enter the price per item in USD: 12.50

Customer Profile: Alice
USD Total: $   50.00
EUR Total: €   46.00

System Complete'''
#part1
cust_name = str(input("What is your name? "))
num_item = float(input("Enter the number of items: "))
price_item = float(input("Enter the price per item in USD: "))

#part2
subtotal = num_item * price_item 
euro = round(subtotal * .92, 2)
#Part3

print("\n \n" "Customer Profile:", cust_name)
print("USD Total: $  ", subtotal)
print("EUR Total: €  ", euro ,"\n \nSystem Complete")