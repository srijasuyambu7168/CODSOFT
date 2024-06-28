import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Can't divide 0 with 0")
        root.after(1300, lambda: entry.delete(0, tk.END))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        root.after(1300, lambda: entry.delete(0, tk.END))


def on_key_press(event):
    if event.char.isdigit() or event.char in "+-*/.":
        entry.insert(tk.END, event.char)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        entry.delete(len(entry.get())-1, tk.END)

entry = tk.Entry(root, font=("Arial", 24), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

entry.bind("<KeyPress>", on_key_press)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
buttons_list = []
for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, font=("Arial", 18), command=calculate)
    else:
        btn = tk.Button(root, text=button, font=("Arial", 18), command=lambda b=button: entry.insert(tk.END, b))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    buttons_list.append(btn)
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i % 4, weight=1)
root.mainloop()
