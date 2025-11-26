import tkinter as tk

Basic_calc = tk.Tk()
Basic_calc.title("Basic Calculator Input Box")
Basic_calc.geometry("400x500")
Basic_calc.config(bg="gray30")

with open("Calculator/ExcessTextStorage.txt", "r") as f:
    txt_content = f.read()

input_box = tk.Text(Basic_calc, font=("Arial", 15))
input_box.insert("1.0", txt_content)
input_box.config(bg="gray", fg="black", borderwidth=2, relief="sunken")
input_box.pack(pady=20,  padx=20, fill="both")

Basic_calc.mainloop()