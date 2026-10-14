
def calculate_payroll():
    total_payroll = 0.0
    while True:
        hourly_wage = float(input("What is the employee's hourly wage? (Enter a negative value to stop): "))
        if hourly_wage < 0:
            break
        hours_worked = float(input("How many hours did the employee work? "))
        if hours_worked > 40:
            regular_pay = 40 * hourly_wage
            overtime_pay = (hours_worked - 40) * hourly_wage * 1.5
            total_pay = regular_pay + overtime_pay
        else:
            total_pay = hours_worked * hourly_wage
        total_payroll += total_pay
    if total_payroll > 5000:
        print("The payroll exceeded the budget.")
    return total_payroll
total_payroll = calculate_payroll()
print(f"Total payroll: ${total_payroll}")