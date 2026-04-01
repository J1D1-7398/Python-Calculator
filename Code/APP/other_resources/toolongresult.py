import tkinter as tk

TooLongTextCalculators = tk.Tk()
TooLongTextCalculators.title("Long Result")
TooLongTextCalculators.geometry("400x500")
TooLongTextCalculators.config(bg="gray30")

with open("other_resources/toolong_calc.txt", "r") as f:
    toolongtextcontent = f.read()

toolongtext = tk.Label(text=toolongtextcontent, master=TooLongTextCalculators, font=("Arial", 15), anchor="nw", justify="left", wraplength=360)
toolongtext.config(bg="gray", fg="black", borderwidth=2, relief="sunken", cursor="arrow")
toolongtext.pack(pady=20,  padx=20, ipady=1000, fill="both")

TooLongTextCalculators.mainloop()