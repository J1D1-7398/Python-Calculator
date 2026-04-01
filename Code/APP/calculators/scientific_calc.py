import tkinter as tk
import os
import math
import subprocess

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
print()
print("Scientific Calculator by J1D1:")
print()
print("This program was only tested on Windows, it may not work on other systems. (Might work on Linux)")
print()
print("Please refer to https://github.com/J1D1-7398/Python-Calculator for more information.")
print()

with open("other_resources/toolong_calc.txt", "w") as f:
    f.write("")

Basic_calc = tk.Tk()
Basic_calc.title("Scientific Calculator")
Basic_calc.geometry("500x600")
Basic_calc.config(bg="black")
Basic_calc.resizable(False, False)

button = tk.Button(Basic_calc, text="☰", bg="gray", fg="black", font=("Sans Serif", 14), borderwidth=3, relief="raised", activebackground="gray45", command=lambda: [Basic_calc.destroy(), subprocess.Popen(["python", "main.py"])])
button.place(relx=0.005, rely=0.005, relwidth=0.09, relheight=0.07)

def press_buttons(key):
    lb.config(text=lb.cget("text") + key)

def press_equal():
    result = calculate()
    lb.config(text=str(result))
def press_clear():
    lb.config(text="")
def press_backspace():
    lb.config(text=lb.cget("text")[:-1])
def open_long_text():
    with open("other_resources/toolong_calc.txt", "w", encoding="utf-8") as f:
        f.write(lb.cget("text"))
    subprocess.Popen(["python", "other_resources/toolongresult.py"])
def calculate():
    expr = lb.cget("text").replace("x", "*").replace("÷", "/").replace("yˣ", "**").replace("√(", "math.sqrt(").replace("x(10yˣ", "*(10**").replace("pi", "math.pi")
    sqrt_count = expr.count("math.sqrt(") - lb.cget("text").count("√")
    expr += ")" * sqrt_count
    try:
        result = eval(expr)
        if isinstance(result, float):
            result = round(result, 10)
    except Exception:
        result = "Error"
    return result

lb = tk.Label(Basic_calc,text="")
lb.config(bg="gray", fg="black", font=("Sans Serif", 30), borderwidth=3, relief="sunken")
lb.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.15)

equalbutton = tk.Button(Basic_calc, text="=", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_equal)
equalbutton.place(relx=0.8, rely=0.9, relwidth=0.2, relheight=0.1)
dotbutton = tk.Button(Basic_calc, text=".", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("."))
dotbutton.place(relx=0.6, rely=0.9, relwidth=0.2, relheight=0.1)
zerobutton = tk.Button(Basic_calc, text="0", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("0"))
zerobutton.place(relx=0.2, rely=0.9, relwidth=0.2, relheight=0.1)
deletebutton = tk.Button(Basic_calc, text="⌫", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_backspace)
deletebutton.place(relx=0, rely=0.9, relwidth=0.2, relheight=0.1)
onebutton = tk.Button(Basic_calc, text="1", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("1"))
onebutton.place(relx=0, rely=0.8, relwidth=0.2, relheight=0.1)
twobutton = tk.Button(Basic_calc, text="2", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("2"))
twobutton.place(relx=0.2, rely=0.8, relwidth=0.2, relheight=0.1)
threebutton = tk.Button(Basic_calc, text="3", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("3"))
threebutton.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1)
plusbutton = tk.Button(Basic_calc, text="+", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("+"))
plusbutton.place(relx=0.8, rely=0.8, relwidth=0.2, relheight=0.1)
fourbutton = tk.Button(Basic_calc, text="4", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("4"))
fourbutton.place(relx=0, rely=0.7, relwidth=0.2, relheight=0.1)
fivebutton = tk.Button(Basic_calc, text="5", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("5"))
fivebutton.place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.1)
sixbutton = tk.Button(Basic_calc, text="6", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("6"))
sixbutton.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.1)
minusbutton = tk.Button(Basic_calc, text="-", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("-"))
minusbutton.place(relx=0.8, rely=0.7, relwidth=0.2, relheight=0.1)
sevenbutton = tk.Button(Basic_calc, text="7", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("7"))
sevenbutton.place(relx=0, rely=0.6, relwidth=0.2, relheight=0.1)
eightbutton = tk.Button(Basic_calc, text="8", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("8"))
eightbutton.place(relx=0.2, rely=0.6, relwidth=0.2, relheight=0.1)
ninebutton = tk.Button(Basic_calc, text="9", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("9"))
ninebutton.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1)
multiplybutton = tk.Button(Basic_calc, text="x", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("x"))
multiplybutton.place(relx=0.8, rely=0.6, relwidth=0.2, relheight=0.1)
clearbutton = tk.Button(Basic_calc, text="C", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_clear)
clearbutton.place(relx=0, rely=0.25, relwidth=0.2, relheight=0.1)
openbutton = tk.Button(Basic_calc, text="(", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("("))
openbutton.place(relx=0.2, rely=0.25, relwidth=0.2, relheight=0.1)
closebutton = tk.Button(Basic_calc, text=")", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons(")"))
closebutton.place(relx=0.4, rely=0.25, relwidth=0.2, relheight=0.1)
dividebutton = tk.Button(Basic_calc, text="÷", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("÷"))
dividebutton.place(relx=0.8, rely=0.5, relwidth=0.2, relheight=0.1)
elevatedbutton = tk.Button(Basic_calc, text="yˣ", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("yˣ"))
elevatedbutton.place(relx=0, rely=0.5, relwidth=0.2, relheight=0.1)
rootbutton = tk.Button(Basic_calc, text="√", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("√("))
rootbutton.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.1)
x10button = tk.Button(Basic_calc, text="x10ˣ", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("x(10yˣ"))
x10button.place(relx=0.4, rely=0.9, relwidth=0.2, relheight=0.1)
pibutton = tk.Button(Basic_calc, text="π", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=lambda: press_buttons("pi"))
pibutton.place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.1)

seemore = tk.Button(Basic_calc, text="See more", bg="gray", fg="black", font=("Sans Serif", 10), borderwidth=3, relief="raised", activebackground="gray40", command=open_long_text)
seemore.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.05)


Basic_calc.mainloop()

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
print()
print("Thank you for using Scientific Calculator by J1D1!")
print()
print("Please refer to https://github.com/J1D1-7398/Python-Calculator for more information.")
print()
