import tkinter as tk
import os

with open("ExcessTextStorage.txt", "w") as f:
    f.write("")

# Basic_calc Window setup
Basic_calc = tk.Tk()
Basic_calc.title("Basic Calculator")
Basic_calc.geometry("400x500")
Basic_calc.config(bg="black")
Basic_calc.resizable(False, False)

# Functions for buttons
def press_1():
    x = lb.cget("text")
    lb.config(text=x+"1")
def press_2():
    x = lb.cget("text")
    lb.config(text=x+"2")
def press_3():
    x = lb.cget("text")
    lb.config(text=x+"3")
def press_4():
    x = lb.cget("text")
    lb.config(text=x+"4")
def press_5():
    x = lb.cget("text")
    lb.config(text=x+"5")
def press_6():
    x = lb.cget("text")
    lb.config(text=x+"6")
def press_7():
    x = lb.cget("text")
    lb.config(text=x+"7")
def press_8():
    x = lb.cget("text")
    lb.config(text=x+"8")
def press_9():
    x = lb.cget("text")
    lb.config(text=x+"9")
def press_0():
    x = lb.cget("text")
    lb.config(text=x+"0")
def press_plus():
    x = lb.cget("text")
    lb.config(text=x+"+")
def press_minus():
    x = lb.cget("text")
    lb.config(text=x+"-")
def press_multiply():
    x = lb.cget("text")
    lb.config(text=x+"x")
def press_divide():
    x = lb.cget("text")
    lb.config(text=x+"÷")
def press_equal():
    result = calculate()
    lb.config(text=str(result))
def press_dot():
    x = lb.cget("text")
    lb.config(text=x+".")
def press_open():
    x = lb.cget("text")
    lb.config(text=x+"(")
def press_close():
    x = lb.cget("text")
    lb.config(text=x+")")
def press_clear():
    lb.config(text="")
def press_backspace():
    x = lb.cget("text")
    y = x[:-1]
    lb.config(text=y)
def open_long_text():
    with open("ExcessTextStorage.txt", "w") as f:
        f.write(lb.cget("text"))
    os.system("python ExcessText.py")
def calculate():
    expr = lb.cget("text")
    expr = expr.replace("x", "*").replace("÷", "/")
    if "//" in expr or "**" in expr:
        return "Error"
    try:
        result = eval(expr)
        if isinstance(result, float):
            result = round(result, 10)
    except Exception:
        result = "Error"
    return result

# Label to display input/output
lb = tk.Label(Basic_calc,text="")
lb.config(bg="gray", fg="black", font=("Sans Serif", 30), borderwidth=3, relief="sunken")
lb.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.15)

# All buttons
button = tk.Button(Basic_calc, text="=", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_equal)
button.place(relx=0.75, rely=0.85, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text=".", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_dot)
button.place(relx=0.5, rely=0.85, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="0", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_0)
button.place(relx=0.25, rely=0.85, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="⌫", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_backspace)
button.place(relx=0, rely=0.85, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="1", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_1)
button.place(relx=0, rely=0.7, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="2", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_2)
button.place(relx=0.25, rely=0.7, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="3", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_3)
button.place(relx=0.5, rely=0.7, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="+", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_plus)
button.place(relx=0.75, rely=0.7, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="4", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_4)
button.place(relx=0, rely=0.55, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="5", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_5)
button.place(relx=0.25, rely=0.55, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="6", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_6)
button.place(relx=0.5, rely=0.55, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="-", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_minus)
button.place(relx=0.75, rely=0.55, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="7", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_7)
button.place(relx=0, rely=0.4, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="8", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_8)
button.place(relx=0.25, rely=0.4, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="9", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_9)
button.place(relx=0.5, rely=0.4, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="x", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_multiply)
button.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="C", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_clear)
button.place(relx=0, rely=0.25, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="(", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_open)
button.place(relx=0.25, rely=0.25, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text=")", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_close)
button.place(relx=0.5, rely=0.25, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="÷", bg="gray", fg="black", font=("Sans Serif", 20), borderwidth=3, relief="raised", activebackground="gray40", command=press_divide)
button.place(relx=0.75, rely=0.25, relwidth=0.25, relheight=0.15)
button = tk.Button(Basic_calc, text="See more", bg="gray", fg="black", font=("Sans Serif", 10), borderwidth=3, relief="raised", activebackground="gray40", command=open_long_text)
button.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.05)


Basic_calc.mainloop()