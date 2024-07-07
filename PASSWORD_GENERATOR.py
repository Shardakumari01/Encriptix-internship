import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length should be a positive integer")
    except ValueError as e:
        label_result.config(text=f"Error: {e}")    
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    label_result.config(text=f"Generated Password: {password}")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

label_prompt = tk.Label(root, text="Enter the desired password length: ")
label_prompt.pack(pady=10)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()