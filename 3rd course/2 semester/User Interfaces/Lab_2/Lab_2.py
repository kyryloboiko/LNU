import tkinter as tk
from tkinter import messagebox

def find_min_element_and_index():
    input_string = entry_array.get()

    if not input_string.strip():
        messagebox.showerror("Error", "Input field is empty. Please enter numbers.")
        label_result.config(text="Result:")
        return

    try:
        processed_string = input_string.replace(',', ' ')
        elements = [item for item in processed_string.split() if item]

        if not elements:
             raise ValueError("Array is empty after processing.")

        numbers = [float(elem) for elem in elements]

    except ValueError:
        messagebox.showerror("Input Error", "Please enter only numbers separated by spaces or commas.")
        label_result.config(text="Result: Invalid input")
        return

    try:
        min_value = min(numbers)
        min_index = numbers.index(min_value)

        if min_value == int(min_value):
            min_value_str = str(int(min_value))
        else:
            min_value_str = str(min_value)

        result_text = f"Result:\nMinimum number: {min_value_str}\nIts index: {min_index}"
        label_result.config(text=result_text)

    except Exception as e:
        messagebox.showerror("Processing Error", f"Something went wrong: {e}")
        label_result.config(text="Result: Error")

# Window
window = tk.Tk()
window.title("Find Minimum in Array")
window.geometry("450x250")

# Text
label_instruction = tk.Label(window, text="Enter numbers separated by spaces or commas:")
label_instruction.pack(pady=10)

# Input
entry_array = tk.Entry(window, width=50)
entry_array.pack(pady=5)

# Function's button
button_calculate = tk.Button(window, text="Find Minimum", command=find_min_element_and_index)
button_calculate.pack(pady=15)

# Result
label_result = tk.Label(window, text="Result:", justify=tk.LEFT, font=("Arial", 11))
label_result.pack(pady=10)

window.mainloop()