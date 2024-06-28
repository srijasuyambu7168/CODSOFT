import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    if not length.isdigit() or int(length) < 1:
        messagebox.showerror("Invalid Input", "Please enter a valid length.")
        return

    length = int(length)
    
    characters = ""
    if var_uppercase.get():
        characters += string.ascii_uppercase
    if var_lowercase.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_special.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Invalid Input", "Please select at least one character set.")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("700x400")
root.configure(bg="#2c3e50")
root.resizable(False, False)

label_font = ("Helvetica", 14, "bold")
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")
button_bg = "#e74c3c"
button_fg = "#ecf0f1"

frame_input = tk.Frame(root, bg="#2c3e50")
frame_input.pack(pady=20)

label_length = tk.Label(frame_input, text="Password Length:", font=label_font, fg="#ecf0f1", bg="#2c3e50")
label_length.grid(row=0, column=0, padx=10, pady=10)

length_var = tk.StringVar()
entry_length = tk.Entry(frame_input, textvariable=length_var, font=entry_font, width=5)
entry_length.grid(row=0, column=1, padx=10, pady=10)

frame_options = tk.Frame(root, bg="#2c3e50")
frame_options.pack(pady=10)

var_uppercase = tk.BooleanVar()
check_uppercase = tk.Checkbutton(frame_options, text="Include Uppercase", variable=var_uppercase, font=label_font, fg="#ecf0f1", bg="#2c3e50", selectcolor="#34495e")
check_uppercase.grid(row=0, column=0, padx=10, pady=5)

var_lowercase = tk.BooleanVar()
check_lowercase = tk.Checkbutton(frame_options, text="Include Lowercase", variable=var_lowercase, font=label_font, fg="#ecf0f1", bg="#2c3e50", selectcolor="#34495e")
check_lowercase.grid(row=0, column=1, padx=10, pady=5)

var_digits = tk.BooleanVar()
check_digits = tk.Checkbutton(frame_options, text="Include Digits", variable=var_digits, font=label_font, fg="#ecf0f1", bg="#2c3e50", selectcolor="#34495e")
check_digits.grid(row=1, column=0, padx=10, pady=5)

var_special = tk.BooleanVar()
check_special = tk.Checkbutton(frame_options, text="Include Special Characters", variable=var_special, font=label_font, fg="#ecf0f1", bg="#2c3e50", selectcolor="#34495e")
check_special.grid(row=1, column=1, padx=10, pady=5)

button_generate = tk.Button(root, text="Generate Password", font=button_font, bg=button_bg, fg=button_fg, command=generate_password)
button_generate.pack(pady=20, padx=20, ipadx=10, ipady=5)

entry_password = tk.Entry(root, font=("Helvetica", 16), width=30, justify="center")
entry_password.pack(pady=10)

root.mainloop()
