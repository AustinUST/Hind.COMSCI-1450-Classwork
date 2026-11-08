
import string
import tkinter as tk
import math as m
import random as r
import time as t
import numpy as np

''' #2
def convert():
    try:
        root2 = tk.Toplevel(root)
        root2.title("Conversion Result")
        root2.geometry("800x700")
        pounds = float(entry.get())
        kilos = pounds * 0.453592
        result_label2 = tk.Label(root2, text=f"Weight in kilograms: {kilos:.2f}")
        result_label2.pack(pady=10)
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")
root = tk.Tk()
root.title("Pounds to Kilograms Converter")
root.geometry("1000x1000")

e1 = tk.Label(root, text="Enter weight in pounds:")
e1.pack()

entry = tk.Entry(root, width=20)
entry.pack(pady=10)


button = tk.Button(root, text="Convert", command=convert)
button.pack(pady=10)

root.mainloop()'''

#1
#evaluate the grade **pass or fail
def evaluate_grade():
    try:
        grade_value = float(grade.get())
        if grade_value >= 60:
            result = f"Pass {course_entry.get()}"
        else:
            result = f"Fail {course_entry.get()}"
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")
    

rootp = tk.Tk()
rootp.title("Course grading tool")
rootp.geometry("1000x1000")
course2 = tk.Label(rootp, text="Enter your course name:")
course2.pack(pady=10)
course_label = tk.Label(rootp, text=f"Course: ")
course_label.pack(pady=10)
course_entry = tk.Entry(rootp, width=20)
course_entry.pack(pady=10)
course1 = course_entry.get()
grade1 = tk.Label(rootp, text="Enter your grade:")
grade1.pack()
grade = tk.Entry(rootp, width=20)
grade.pack(pady=10)
entry = tk.Entry(rootp, width=20)
entry.pack(pady=10)
result_label = tk.Label(rootp, text="")
result_label.pack(pady=10)
button = tk.Button(rootp, text="Evaluate", command=evaluate_grade)
button.pack(pady=10)
exit_button = tk.Button(rootp, text="Exit", command=rootp.destroy)
exit_button.pack(pady=10)

rootp.mainloop()

#3
'''Create a window featuring a header text label that says: "Select your dietary preferences:".
Requirements
• Checkboxes: Add three explicit checkbuttons labeled Vegetarian, Gluten-Free,
and Nut-Free.
• Action Button: Place a Submit button at the bottom of the window layout.
• Label Summary: When clicked, display in a label a list containing only the
specific options the user selected.'''

def submit_preferences():
    selected_options = []
    if vegetarian_button.get():
        selected_options.append("Vegetarian")
    if gluten_free_button.get():
        selected_options.append("Gluten-Free")
    if nut_free_button.get():
        selected_options.append("Nut-Free")
    summary_label.config(text="Selected Preferences: " + ", ".join(selected_options))
    
rootw = tk.Tk()
rootw.title("Dietary Preferences")
rootw.geometry("400x300")
vegetarian_button = tk.Checkbutton(rootw, text="Vegetarian")
vegetarian_button.pack(pady=5)
gluten_free_button = tk.Checkbutton(rootw, text="Gluten-Free")
gluten_free_button.pack(pady=5)
nut_free_button = tk.Checkbutton(rootw, text="Nut-Free")
nut_free_button.pack(pady=5)
summary_label = tk.Label(rootw, text="")
summary_label.pack(pady=10)
submit_button = tk.Button(rootw, text="Submit", command=submit_preferences)
submit_button.pack(pady=10)

rootw.mainloop()
