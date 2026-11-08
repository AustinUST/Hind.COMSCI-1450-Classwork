import tkinter as tk


'''Part 1: Overall Window & Menu Architecture

Your application must create a single parent window with a dropdown menu bar for
screen navigation using a universal framework.
1. Main Window Setup
• Title: Set the main window title to "Personal Health & Travel Assistant".
• Size: Set the window geometry to 500x400 pixels.
• System Tracking Label: Add a global tk.Label at the very top of the window
structure to display status messages (e.g., "Select an application from the top
menu to begin").

2. Core Navigation Function
You must write a structural tracking function matching this exact signature pattern to
manage view states:
python
def show_page(frame_to_show):
"""Hides all application pages, then packs the chosen one."""
fitness_page.pack_forget()
flight_page.pack_forget()
frame_to_show.pack(fill="both", expand=True, padx=20, pady=20)

3. Menu Bar Configuration
Implement a standard system menu bar (tk.Menu) at the top of the interface featuring
two primary dropdown structures:
• File Dropdown Menu:
o Command 1: "Reset Activity Logs" (linked to a clean-up routine function
that clears out file data history).
o Command 2: "Exit Application"
• Applications Dropdown Menu: Use lambda arguments to call your page
management utility function:
o Command 1: "Fitness Tracker"
o Command 2: "Flight Fare Estimator'''


import tkinter as tk

root = tk.Tk()
root.title("Personal Health & Travel Assistant")
root.geometry("500x400")
status_label = tk.Label(root, text="Select an application from the top menu to begin")
status_label.pack(side="top", fill="x")
fitness_page = tk.Frame(root)
tk.Label(fitness_page, text="Fitness Tracker").pack()

flight_page = tk.Frame(root)
tk.Label(flight_page, text="Flight Fare Estimator").pack()

def show_page(frame_to_show):
    """Hides all application pages, then packs the chosen one."""
    fitness_page.pack_forget()
    flight_page.pack_forget()
    frame_to_show.pack(fill="both", expand=True, padx=20, pady=20)

def reset_logs():
    status_label.config(text="Activity logs reset")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Reset Activity Logs", command=reset_logs)
file_menu.add_command(label="Exit Application", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

applications_menu = tk.Menu(menu_bar, tearoff=0)
applications_menu.add_command(label="Fitness Tracker", command=lambda: show_page(fitness_page))
applications_menu.add_command(label="Flight Fare Estimator", command=lambda: show_page(flight_page))
menu_bar.add_cascade(label="Applications", menu=applications_menu)

root.config(menu=menu_bar)
root.mainloop()