import pandas as pd
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox


FILE_NAME = "sample.csv"


try:
    df = pd.read_csv(FILE_NAME)
except FileNotFoundError:
    messagebox.showerror("Error", f"File '{FILE_NAME}' not found!\nPlease check the file name and location.")
    exit()

# for cheking required column
required = ['student_id', 'js', 'py', 'ds']
missing = [col for col in required if col not in df.columns]
if missing:
    messagebox.showerror("Missing Columns", f"These columns are missing: {', '.join(missing)}")
    exit()

# GUI

root = tk.Tk()
root.title("Student Data Search")
root.geometry("650x550")
root.resizable(False, False)

heading = tk.Label(root, text="Student Data Search", font=("Arial", 18, "bold"))
heading.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter Roll Number:", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

roll_entry = tk.Entry(input_frame, font=("Arial", 12), width=15)
roll_entry.pack(side=tk.LEFT, padx=5)
roll_entry.focus()

result_text = scrolledtext.ScrolledText(root, width=70, height=20, font=("Consolas", 11), wrap=tk.WORD)
result_text.pack(pady=15, padx=20)

def search_student():
    roll_input = roll_entry.get().strip()
    
    if not roll_input:
        messagebox.showwarning("Input Required", "Please enter a Roll Number!")
        return
    
    if not roll_input.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid number!")
        return
    
    roll = int(roll_input)
    
    student = df[df['student_id'] == roll]
    
    result_text.delete(1.0, tk.END) 
    
    if student.empty:
        result_text.insert(tk.END, f"No data found for Roll Number {roll}.\n")
        result_text.config(fg="red")
        return
    
    result_text.config(fg="black")
    
    # convert student data into dictionary
    student_data = student.iloc[0].to_dict()
    
    # calculate total marks
    js = student_data.get('js', 0)        
    python = student_data.get('py', 0)
    ds = student_data.get('ds', 0)       
    total_marks = js + python + ds
    
    # Display
    result_text.insert(tk.END, f"{'-'*60}\n")
    result_text.insert(tk.END, f"             Roll No : {roll}\n")
    result_text.insert(tk.END, f"{'-'*60}\n\n")
    
    for col, value in student_data.items():
        display_name = col.replace('_', ' ').title()
        result_text.insert(tk.END, f"{display_name:<25}: {value}\n")
    
    # Calculated total show
    result_text.insert(tk.END, "\n")
    result_text.insert(tk.END, f"{'-'*60}\n")
    result_text.insert(tk.END, f"Total Marks (calculated) : {total_marks}\n")
    result_text.insert(tk.END, f"{'-'*60}\n\n")

def clear():
    roll_entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)
    roll_entry.focus()

def exit_program():
    root.destroy()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

search_btn = tk.Button(button_frame, text="Search", font=("Arial", 12), width=12, bg="#4CAF50", fg="white", command=search_student)
search_btn.pack(side=tk.LEFT, padx=10)

clear_btn = tk.Button(button_frame, text="Clear", font=("Arial", 12), width=12, bg="#2196F3", fg="white", command=clear)
clear_btn.pack(side=tk.LEFT, padx=10)

exit_btn = tk.Button(button_frame, text="Exit", font=("Arial", 12), width=12, bg="#f44336", fg="white", command=exit_program)
exit_btn.pack(side=tk.LEFT, padx=10)

root.bind('<Return>', lambda event: search_student())

root.mainloop()