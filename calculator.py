# project 2- calculator
import tkinter as tk
from tkinter import messagebox

# Function to perform calculation based on operation
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero!")
            return
        else:
            result = num1 / num2
    else:
        messagebox.showerror("Error", "Invalid operation")
        return
    
    entry_result.delete(0, tk.END)  # Clear the previous result
    entry_result.insert(0, result)  # Insert the new result

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Variables for operation choice
operation_var = tk.StringVar(root)
operation_var.set('+')  # Default operation choice

# Labels and entry widgets for user input
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

label_operation = tk.Label(root, text="Select operation:")
label_operation.grid(row=2, column=0, padx=10, pady=10)
option_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
option_menu.grid(row=2, column=1, padx=10, pady=10)

# Button to calculate the result
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Label and entry widget to display the result
label_result = tk.Label(root, text="Result:")
label_result.grid(row=4, column=0, padx=10, pady=10)
entry_result = tk.Entry(root)
entry_result.grid(row=4, column=1, padx=10, pady=10)

# Start the tkinter main loop
root.mainloop()
