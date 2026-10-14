
def calculate_ticket_sales():
    total_sales = 0.0
    tickets_sold = 0
    while True:
        age = int(input("Enter your age (-1 to exit): "))
        if age == -1:
            break
        if age < 5:
            ticket_price = 0.00
        elif 5 <= age <= 12:
            ticket_price = 8.00
        elif 13 <= age <= 59:
            ticket_price = 12.00
        else:
            ticket_price = 9.00
        total_sales += ticket_price
        tickets_sold += 1
    if tickets_sold >= 10:
        total_sales *= 0.95
    return total_sales, tickets_sold
total, tickets = calculate_ticket_sales()
print(f"Total tickets sold: {tickets}")
print(f"Final sales amount: ${total}")