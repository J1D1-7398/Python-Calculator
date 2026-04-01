import os
import sys
import subprocess
import tkinter as tk
from tkinter import ttk

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
print()
print("Multi Calculator by J1D1:")
print()
print("This program was only tested on Windows, it may not work on other systems. (Might work on Linux)")
print()
print("Please refer to https://github.com/J1D1-7398/Python-Calculator for more information.")
print()

menu = tk.Tk()
menu.title("Calculator Menu")
menu.geometry("400x500")
menu.config(bg="gray30")

rickrolled = False

calctype = tk.StringVar()
select_calc = ttk.Combobox(menu, values=["None Selected","Basic Calculator", "Scientific Calculator", "Areas", "Volumes", "Perimeters", "Pythagorean Theorem", "Second Degree Equations", "Trigonometry", "Functions", "Proportions", "Simple Interest", "Compound Interest"])
select_calc.set("None Selected")
select_calc.bind("<<ComboboxSelected>>")
select_calc.config(font=("Arial", 12))
select_calc['state'] = 'readonly'
select_calc.place(relx=0.14, rely=0.2, relwidth=0.70, relheight=0.06)

def select_calculator_type(event):
    calctype.set(select_calc.get())
    if calctype.get() == "Basic Calculator":
        Select.config(command=lambda: [menu.destroy(), subprocess.Popen(["python", "calculators/basic_calc.py"])])
    elif calctype.get() == "Scientific Calculator":
        Select.config(command=lambda: [menu.destroy(), subprocess.Popen(["python", "calculators/scientific_calc.py"])])
    elif calctype.get() == "Areas":
        Select.config(command=lambda: [menu.destroy(), subprocess.Popen(["python", "geometry/areas.py"])])
    elif calctype.get() == "Volumes":
        Select.config(command=lambda: [menu.destroy(), subprocess.Popen(["python", "geometry/volumes.py"])])
    elif calctype.get() == "Perimeters":
        Select.config(command=lambda: [menu.destroy(), subprocess.Popen(["python", "geometry/perimeters.py"])])
    elif calctype.get() == "Pythagorean Theorem":
        Select.config(command=lambda: [menu.destroy(), subprocess.Popen(["python", "compound_calculators/pythagorean.py"])])
    elif calctype.get() == "Second Degree Equations":
        Select.config(command=lambda: [menu.destroy(), subprocess.Popen(["python", "compound_calculators/seconddegreeequations.py"])])
    elif calctype.get() == "Trigonometry":
        Select.config(command=lambda: [menu.destroy(), subprocess.Popen(["python", "compound_calculators/trigonometry.py"])])
    elif calctype.get() == "Functions":
        Select.config(command=lambda: [menu.destroy(), subprocess.Popen(["python", "compound_calculators/functions.py"])])
    elif calctype.get() == "Simple Interest":
        Select.config(command=lambda: [menu.destroy(), subprocess.Popen(["python", "finances/simple_interest.py"])])
    elif calctype.get() == "Compound Interest":
        Select.config(command=lambda: [menu.destroy(), subprocess.Popen(["python", "finances/compound_interest.py"])])
    elif calctype.get() == "Proportions":
        Select.config(command=lambda: [menu.destroy(), subprocess.Popen(["python", "compound_calculators/proportions.py"])])
    elif calctype.get() == "None Selected":
        if sys.platform == "win32":
            Select.config(command=lambda: [menu.destroy(), subprocess.Popen(["start", "other_resources\\BaseErrorCalc.mp4"], shell=True)])
        else:
            Select.config(command=lambda: [menu.destroy(), subprocess.Popen(["xdg-open", "other_resources/BaseErrorCalc.mp4"])])
        global rickrolled
        rickrolled = True
select_calc.bind("<<ComboboxSelected>>", select_calculator_type)

Select = tk.Button(menu, text="Select", bg="gray", fg="black", font=("Arial", 12), borderwidth=3, relief="raised", activebackground="gray40")
Select.place(relx=0.2, rely=0.7)
Close = tk.Button(menu, text="Close", bg="gray", fg="black", font=("Arial", 12), borderwidth=3, relief="raised", activebackground="gray40", command=menu.destroy)
Close.place(relx=0.6, rely=0.7)

menu.mainloop()


subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
print()
print("Thank you for using Multi Calculator by J1D1!")
print()
print("Please refer to https://github.com/J1D1-7398/Python-Calculator for more information.")
print()
if rickrolled == True:
    print("XD You Got Rickrolled!")
    print()