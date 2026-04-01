import tkinter as tk
import subprocess
import os
secondequations_calc = tk.Tk()
secondequations_calc.title("Second Degree Equations Calculator")
secondequations_calc.geometry("500x200")
secondequations_calc.config(bg="gray20")
secondequations_calc.resizable(False, False)

button = tk.Button(secondequations_calc, text="☰", bg="gray", fg="black", font=("Sans Serif", 14), borderwidth=3, relief="raised", activebackground="gray45", command=lambda: [secondequations_calc.destroy(), subprocess.Popen(["python", "main.py"])])
button.place(relx=0.005, rely=0.005, relwidth=0.065, relheight=0.13)

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
print()
print("Second Degree Equations Calculator by J1D1:")
print()
print("This program was only tested on Windows, it may not work on other systems. (Might work on Linux)")
print()
print("Please refer to https://github.com/J1D1-7398/Python-Calculator for more information.")
print()


def completeequation():
    selectedtype.config(text="Complete Equation")
    avalue.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.15)
    bvalue.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.15)
    cvalue.place(relx=0.2, rely=0.5, relwidth=0.6, relheight=0.15)
    clabel.place(relx=0.14, rely=0.5, relwidth=0.06, relheight=0.15)
    blabel.place(relx=0.14, rely=0.35, relwidth=0.06, relheight=0.15)
    equalbutton.place(relheight=0.6)
def apluscequation():
    selectedtype.config(text="A & C Equation")
    blabel.place_forget()
    bvalue.place_forget()
    avalue.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.15)
    cvalue.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.15)
    clabel.place(relx=0.14, rely=0.35, relwidth=0.06, relheight=0.15)
def aplusbequation():
    selectedtype.config(text="A & B Equation")
    clabel.place_forget()
    cvalue.place_forget()
    avalue.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.15)
    bvalue.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.15)
    equalbutton.place(relheight=0.45)
x = 0
def changetype():
    global x
    x = x + 1
    resultlabel1.place_forget()
    resultlabel2.place_forget()
    avalue.delete(0, tk.END)
    bvalue.delete(0, tk.END)
    cvalue.delete(0, tk.END)
    if x > 2:
        x = 0
    if x == 0:
        completeequation()
    if x == 1:
        aplusbequation()
    if x == 2:
        apluscequation()

def solve():
    try:
        if x == 0:
            a = int(avalue.get())
            b = int(bvalue.get())
            c = int(cvalue.get())
            resultlabel1.place(relx=0.14, rely=0.65, relwidth=0.76, relheight=0.15)
            resultlabel2.place(relx=0.14, rely=0.8, relwidth=0.76, relheight=0.15)
            if (b**2-4*a*c) < 0:
                resultlabel1.config(text="No real solutions", anchor="w")
                print("No real solutions")
            else:
                resultlabel1.config(text=((b*-1)+((b)**2-4*a*c)**0.5)/2*a, anchor="w")
                resultlabel2.config(text=((b*-1)-((b)**2-4*a*c)**0.5)/2*a, anchor="w")
                print(((b*-1)+((b)**2-4*a*c)**0.5)/2*a)
                print(((b*-1)-((b)**2-4*a*c)**0.5)/2*a)
        if x == 1:
            a = int(avalue.get())
            b = int(bvalue.get())
            resultlabel1.place(relx=0.14, rely=0.5, relwidth=0.76, relheight=0.15)
            resultlabel2.place(relx=0.14, rely=0.65, relwidth=0.76, relheight=0.15)
            resultlabel1.config(text=-1*b/a, anchor="w")
            print(-1*b/a)
        if x == 2:
            a = int(avalue.get())
            c = int(cvalue.get())
            resultlabel1.place(relx=0.14, rely=0.5, relwidth=0.76, relheight=0.15)
            resultlabel2.place(relx=0.14, rely=0.65, relwidth=0.76, relheight=0.15)
            if (-1*(c/a)) < 0:
                resultlabel1.config(text="No real solutions", anchor="w")
                print("No real solutions")
            else:
                resultlabel1.config(text=(-1*(c/a))**0.5, anchor="w")
                resultlabel2.config(text=-1*((-1*(c/a))**0.5), anchor="w")
                print((-1*(c/a))**0.5)
                print(-1*((-1*(c/a))**0.5))
    except Exception as e:
        resultlabel1.config(text="Please fill in all the gaps and check if all the characters are numbers!", anchor="w")
        print("Please fill in all the gaps and check if all the characters are numbers!")
        print("---------------")
        print(e)
        print("---------------")



rotate = tk.Button(secondequations_calc, text="⇄", bg="gray", fg="black", font=("Sans Serif", 18), borderwidth=3, relief="raised", activebackground="gray45", command=lambda: changetype())
rotate.place(relx=0.14, rely=0.05, relwidth=0.06, relheight=0.15)

equalbutton = tk.Button(secondequations_calc, text="=", bg="gray", fg="black", font=("Sans Serif", 18), borderwidth=3, relief="raised", activebackground="gray45", command=lambda: solve())
equalbutton.place(relx=0.8, rely=0.05, relwidth=0.1, relheight=0.6)

selectedtype = tk.Label(secondequations_calc, text="Complete Equation", borderwidth=3, relief="raised", bg="gray", fg="black", font=("Sans Serif", 14))
selectedtype.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.15)

alabel = tk.Label(secondequations_calc, text="ax²", borderwidth=3, relief="raised", bg="gray", fg="black", font=("Sans Serif", 12))
alabel.place(relx=0.14, rely=0.2, relwidth=0.06, relheight=0.15)
blabel = tk.Label(secondequations_calc, text="bx", borderwidth=3, relief="raised", bg="gray", fg="black", font=("Sans Serif", 12))
blabel.place(relx=0.14, rely=0.35, relwidth=0.06, relheight=0.15)
clabel = tk.Label(secondequations_calc, text="c", borderwidth=3, relief="raised", bg="gray", fg="black", font=("Sans Serif", 12))
clabel.place(relx=0.14, rely=0.5, relwidth=0.06, relheight=0.15)

avalue = tk.Entry(secondequations_calc, font=("Sans Serif", 14), borderwidth=3, relief="raised", background="gray", foreground="black", cursor="arrow")
bvalue = tk.Entry(secondequations_calc, font=("Sans Serif", 14), borderwidth=3, relief="raised", background="gray", foreground="black", cursor="arrow")
cvalue = tk.Entry(secondequations_calc, font=("Sans Serif", 14), borderwidth=3, relief="raised", background="gray", foreground="black", cursor="arrow")
resultlabel1 = tk.Label(secondequations_calc, text="", borderwidth=3, relief="raised", bg="gray", fg="black", font=("Sans Serif", 12))
resultlabel2 = tk.Label(secondequations_calc, text="", borderwidth=3, relief="raised", bg="gray", fg="black", font=("Sans Serif", 12))


completeequation()
secondequations_calc.mainloop()

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
print()
print("Thank you for using Second Degree Equations Calculator by J1D1!")
print()
print("Please refer to https://github.com/J1D1-7398/Python-Calculator for more information.")
print()
