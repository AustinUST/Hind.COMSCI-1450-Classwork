import tkinter as tk

root = tk.Tk()
root.title("Personal Health & Travel Assistant")
root.geometry("500x400")

status_label = tk.Label(root, text="Select an application from the top menu to begin",
                        font=("Arial", 10), fg="black")
status_label.pack(side="top", fill="x", pady=5)


fitness_page = tk.Frame(root)
flight_page = tk.Frame(root)


def show_page(frame_to_show):
    """Hides all application pages, then packs the chosen one."""
    fitness_page.pack_forget()
    flight_page.pack_forget()
    frame_to_show.pack(fill="both", expand=True, padx=20, pady=20)


def reset_logs():
    """Wipes user_logs.txt by opening it in write mode and closing it."""
    file = open("user_logs.txt", "w")
    file.close()
    status_label.config(text="System Activity Logs Reset Successfully!", fg="dark green")


menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Reset Activity Logs", command=reset_logs)
file_menu.add_command(label="Exit Application", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)

apps_menu = tk.Menu(menu_bar, tearoff=0)
apps_menu.add_command(label="Fitness Tracker", command=lambda: show_page(fitness_page))
apps_menu.add_command(label="Flight Fare Estimator", command=lambda: show_page(flight_page))
menu_bar.add_cascade(label="Applications", menu=apps_menu)

root.config(menu=menu_bar)

# ---------------------------------------------------------------
# Part 2, Page 1: Fitness Page
# ---------------------------------------------------------------
intensity_var = tk.StringVar(value="Low")

activity_label = tk.Label(fitness_page, text="Activity Name:")
activity_label.grid(row=0, column=0, sticky="w", pady=5)

activity_entry = tk.Entry(fitness_page, width=25)
activity_entry.grid(row=0, column=1, sticky="w", pady=5)

duration_label = tk.Label(fitness_page, text="Duration (Minutes):")
duration_label.grid(row=1, column=0, sticky="w", pady=5)

duration_entry = tk.Entry(fitness_page, width=25)
duration_entry.grid(row=1, column=1, sticky="w", pady=5)

intensity_label = tk.Label(fitness_page, text="Intensity:")
intensity_label.grid(row=2, column=0, sticky="nw", pady=5)

low_radio = tk.Radiobutton(fitness_page, text="Low (5 cal/min)",
                           variable=intensity_var, value="Low")
low_radio.grid(row=2, column=1, sticky="w")

medium_radio = tk.Radiobutton(fitness_page, text="Medium (8 cal/min)",
                              variable=intensity_var, value="Medium")
medium_radio.grid(row=3, column=1, sticky="w")

high_radio = tk.Radiobutton(fitness_page, text="High (12 cal/min)",
                            variable=intensity_var, value="High")
high_radio.grid(row=4, column=1, sticky="w")


def log_workout():
    """Validates input, calculates calories burned, and logs the workout."""
    activity = activity_entry.get().strip()
    duration_text = duration_entry.get().strip()

   
    if activity == "" or duration_text == "":
        fitness_result_label.config(text="Warning: Please complete all fields!", fg="red")
        return

    try:
        minutes = int(duration_text)
        if minutes < 0:
            raise ValueError
    except ValueError:
        fitness_result_label.config(text="Warning: Duration must be a whole number of minutes!",
                                    fg="red")
        return

    multipliers = {"Low": 5, "Medium": 8, "High": 12}
    calories = minutes * multipliers[intensity_var.get()]

    fitness_result_label.config(text="Logged: " + activity + " for " + str(calories) + " Calories!",
                                fg="black")

    # File persistence
    file = open("user_logs.txt", "a")
    file.write("[FITNESS] Activity: " + activity + " | Calories Burned: " + str(calories) + "\n")
    file.close()


log_button = tk.Button(fitness_page, text="Log Workout", command=log_workout)
log_button.grid(row=5, column=0, columnspan=2, pady=10)

fitness_result_label = tk.Label(fitness_page, text="")
fitness_result_label.grid(row=6, column=0, columnspan=2, pady=5)


baggage_var = tk.IntVar()
meal_var = tk.IntVar()
priority_var = tk.IntVar()

price_label = tk.Label(flight_page, text="Base Ticket Price ($):")
price_label.grid(row=0, column=0, sticky="w", pady=5)

price_entry = tk.Entry(flight_page, width=20)
price_entry.grid(row=0, column=1, sticky="w", pady=5)

baggage_check = tk.Checkbutton(flight_page, text="Checked Baggage (+$35.00)",
                               variable=baggage_var)
baggage_check.grid(row=1, column=0, columnspan=2, sticky="w")

meal_check = tk.Checkbutton(flight_page, text="In-Flight Meal (+$15.00)",
                            variable=meal_var)
meal_check.grid(row=2, column=0, columnspan=2, sticky="w")

priority_check = tk.Checkbutton(flight_page, text="Priority Boarding (+$20.00)",
                                variable=priority_var)
priority_check.grid(row=3, column=0, columnspan=2, sticky="w")


def calculate_fare():
    """Calculates the total fare with upgrades and logs the result."""
    price_text = price_entry.get().strip()

    if price_text == "":
        fare_output_label.config(text="Warning: Base ticket price is required!", fg="red")
        return

    try:
        base_price = float(price_text)
        total = base_price
        total += baggage_var.get() * 35.00
        total += meal_var.get() * 15.00
        total += priority_var.get() * 20.00

        fare_output_label.config(text="Total Fare: $" + format(total, ".2f"), fg="black")

       
        file = open("user_logs.txt", "a")
        file.write("[FLIGHT] Base: " + format(base_price, ".2f") +
                   " | Total Fare: " + format(total, ".2f") + "\n")
        file.close()
    except ValueError:
        fare_output_label.config(text="Error: Please enter a numeric base price!", fg="red")


fare_button = tk.Button(flight_page, text="Calculate Total Fare", command=calculate_fare)
fare_button.grid(row=4, column=0, columnspan=2, pady=10)

fare_output_label = tk.Label(flight_page, text="", font=("Arial", 12, "bold"))
fare_output_label.grid(row=5, column=0, columnspan=2, pady=5)

show_page(fitness_page)
root.mainloop()