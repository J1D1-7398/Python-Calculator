import tkinter as tk
import subprocess
import os

pythagorean_calc = tk.Tk()
pythagorean_calc.title("Pythagorean Theorem Calculator")
pythagorean_calc.geometry("400x500")
pythagorean_calc.config(bg="gray20")
pythagorean_calc.resizable(False, False)

button = tk.Button(pythagorean_calc, text="☰", bg="gray", fg="black", font=("Sans Serif", 14), borderwidth=3, relief="raised", activebackground="gray45", command=lambda: [pythagorean_calc.destroy(), subprocess.Popen(["python", "main.py"])])
button.place(relx=0.005, rely=0.005, relwidth=0.09, relheight=0.07)

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
print()
print("Pythagorean Theorem Calculator by J1D1:")
print()
print("This program was only tested on Windows, it may not work on other systems. (Might work on Linux)")
print()
print("Please refer to https://github.com/J1D1-7398/Python-Calculator for more information.")
print()


selected = 0
def optionnumber():
    resultlabel.place_forget()
    resultnum.place_forget()
    seemore.place_forget()
    global selected
    selected = selected + 1
    if selected > 2:
        selected = 1
    if selected == 1:
        doubcath()
    if selected == 2:
        cathandhyp()

def doubcath():
    hypotenuse.place_forget()
    cathetus2.place(relx=0.305, rely=0.4, relwidth=0.39, relheight=0.07)
    currentoption.config(text="Cathetus + Cathetus")
    cathetus1.config(text="First Cathetus")
    entry1.place(relx=0.305, rely=0.3, relwidth=0.39, relheight=0.07)
    entry2.place(relx=0.305, rely=0.5, relwidth=0.39, relheight=0.07)
    calculate.place(relx=0.725, rely=0.2, relwidth=0.15, relheight=0.37)

def cathandhyp():
    cathetus2.place_forget()
    hypotenuse.place(relx=0.305, rely=0.4, relwidth=0.39, relheight=0.07)
    currentoption.config(text="Cathetus + Hypotenuse")
    cathetus1.config(text="Cathetus")

def calculateresult():
    resultlabel.place(relx=0.305, rely=0.6, relwidth=0.39, relheight=0.07)
    resultnum.place(relx=0.305, rely=0.7, relwidth=0.39, relheight=0.07)
    seemore.place(relx=0.4, rely=0.78, relwidth=0.2, relheight=0.05)
    if selected == 1:
        resultlabel.config(text="Hypotenuse:")
    elif selected == 2:
        resultlabel.config(text="Second Cathetus:")
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if selected == 1:
            result = (num1**2 + num2**2)**0.5
        elif selected == 2:
            result = (num2**2 - num1**2)**0.5
        resultnum.config(text=result, anchor=tk.W)
    except:
        resultnum.config(text="Invalid input")

def open_long_text():
    with open("other_resources/toolong_calc.txt", "w") as f:
        f.write(str(resultnum.cget("text")))
    subprocess.Popen(["python", "other_resources/toolongresult.py"])

rotate = tk.Button(pythagorean_calc, text="⇄", bg="gray", fg="black", font=("Sans Serif", 18), borderwidth=3, relief="raised", activebackground="gray45", command=lambda: optionnumber())
rotate.place(relx=0.185, rely=0.1, relwidth=0.09, relheight=0.07)

currentoption = tk.Button(pythagorean_calc, text="None", bg="gray", fg="black", borderwidth=3, relief="raised", font=("Sans Serif", 10), activebackground="gray45", disabledforeground="black")
currentoption.config(state="disabled")
currentoption.place(relx=0.285, rely=0.1, relwidth=0.43, relheight=0.07)

cathetus1 = tk.Button(pythagorean_calc, text="First Cathetus", bg="gray", fg="black", borderwidth=3, relief="raised", font=("Sans Serif", 12), activebackground="gray45", disabledforeground="black")
cathetus1.config(state="disabled")
cathetus1.place(relx=0.305, rely=0.2, relwidth=0.39, relheight=0.07)

cathetus2 = tk.Button(pythagorean_calc, text="Second Cathetus", bg="gray", fg="black", borderwidth=3, relief="raised", font=("Sans Serif", 12), activebackground="gray45", disabledforeground="black")
cathetus2.config(state="disabled")
cathetus2.place(relx=0.305, rely=0.3, relwidth=0.39, relheight=0.07)

entry1 = tk.Entry(pythagorean_calc, bg="gray", fg="black", borderwidth=3, relief="raised", font=("Sans Serif", 12), cursor="arrow")
entry1.place_forget()

hypotenuse = tk.Button(pythagorean_calc, text="Hypotenuse", bg="gray", fg="black", borderwidth=3, relief="raised", font=("Sans Serif", 12), activebackground="gray45", disabledforeground="black")
hypotenuse.config(state="disabled")
hypotenuse.place(relx=0.305, rely=0.4, relwidth=0.39, relheight=0.07)

entry2 = tk.Entry(pythagorean_calc, bg="gray", fg="black", borderwidth=3, relief="raised", font=("Sans Serif", 12), cursor="arrow")
entry2.place_forget()

calculate = tk.Button(pythagorean_calc, text="=", bg="gray", fg="black", borderwidth=3, relief="raised", font=("Sans Serif", 15), activebackground="gray45", command=lambda: calculateresult())
calculate.place_forget()

resultlabel = tk.Button(pythagorean_calc, text="", bg="gray", fg="black", borderwidth=3, relief="raised", font=("Sans Serif", 12), activebackground="gray45", disabledforeground="black")
resultlabel.config(state="disabled")
resultlabel.place_forget()

resultnum = tk.Button(pythagorean_calc, text="", bg="gray", fg="black", borderwidth=3, relief="raised", font=("Sans Serif", 12), activebackground="gray45", disabledforeground="black")
resultnum.config(state="disabled")
resultnum.place_forget()
seemore = tk.Button(pythagorean_calc, text="See more", bg="gray", fg="black", font=("Sans Serif", 10), borderwidth=3, relief="raised", activebackground="gray40", command=open_long_text)
seemore.place_forget()


pythagorean_calc.mainloop()

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
print()
print("Thank you for using Pythagorean Theorem by J1D1!")
print()
print("Please refer to https://github.com/J1D1-7398/Python-Calculator for more information.")
print()
