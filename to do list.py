import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def update_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        new_task = entry_task.get()
        if new_task:
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, new_task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    except:
        messagebox.showwarning("Warning", "You must select a task to update.")

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

def save_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Info", "Tasks saved successfully.")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No saved tasks found.")

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")
root.configure(bg="#34495e")

label_font = ("Helvetica", 14, "bold")
button_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 12)
button_bg = "#e74c3c"
button_fg = "#ecf0f1"
label_title = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#34495e", fg="#ecf0f1")
label_title.pack(pady=10)

frame = tk.Frame(root, bg="#34495e")
frame.pack(pady=20)

entry_task = tk.Entry(frame, font=entry_font, width=25)
entry_task.grid(row=0, column=0, padx=10, pady=10)

button_add_task = tk.Button(frame, text="Add Task", font=button_font, bg=button_bg, fg=button_fg, command=add_task)
button_add_task.grid(row=0, column=1, padx=10, pady=10)

listbox_tasks = tk.Listbox(root, font=entry_font, width=40, height=10, bg="#ecf0f1", fg="#34495e", selectbackground="#2c3e50", selectforeground="#ecf0f1")
listbox_tasks.pack(pady=20)

frame_buttons = tk.Frame(root, bg="#34495e")
frame_buttons.pack(pady=10)

button_update_task = tk.Button(frame_buttons, text="Update Task", font=button_font, bg=button_bg, fg=button_fg, command=update_task)
button_update_task.grid(row=0, column=0, padx=10, pady=10)

button_delete_task = tk.Button(frame_buttons, text="Delete Task", font=button_font, bg=button_bg, fg=button_fg, command=delete_task)
button_delete_task.grid(row=0, column=1, padx=10, pady=10)

button_clear_tasks = tk.Button(frame_buttons, text="Clear All Tasks", font=button_font, bg=button_bg, fg=button_fg, command=clear_tasks)
button_clear_tasks.grid(row=1, column=0, padx=10, pady=10)

button_save_tasks = tk.Button(frame_buttons, text="Save Tasks", font=button_font, bg=button_bg, fg=button_fg, command=save_tasks)
button_save_tasks.grid(row=1, column=1, padx=10, pady=10)

button_load_tasks = tk.Button(frame_buttons, text="Load Tasks", font=button_font, bg=button_bg, fg=button_fg, command=load_tasks)
button_load_tasks.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
