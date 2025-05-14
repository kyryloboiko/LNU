import tkinter as tk
from tkinter import ttk
import math

def calculate_function(x):
    return x - 2 + math.sin(1/x)

def tabulate_function():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        step_size = float(entry_step.get())

        if a >= b:
            result_text.set("Error: a must be less than b")
            return
        if step_size <= 0:
            result_text.set("Error: Step size must be greater than 0")
            return

        n = int((b - a) / step_size) + 1  # Calculate the number of points
        x_values = [a + i * step_size for i in range(n)]
        y_values = [calculate_function(x) for x in x_values]

        # Display results in the text area
        text_output.delete(1.0, tk.END)  # Clear previous content
        text_output.insert(tk.END, "Tabulation Results:\n")
        for x, y in zip(x_values, y_values):
            text_output.insert(tk.END, f"x = {x:.4f}, f(x) = {y:.6f}\n")
            print(f"x = {x:.4f}, f(x) = {y:.6f}")


        result_text.set("Tabulation complete. Results displayed below.")

    except ValueError:
        result_text.set("Error: Invalid input. Please enter numbers.")
    except Exception as e:
        result_text.set(f"An error occurred: {e}")

# Main window
window = tk.Tk()
window.title("Function Tabulation")
window.geometry("800x600")

# Input frame
frame = ttk.Frame(window, padding="10")
frame.pack(fill="both", expand=True)

# Labels and entry fields
label_a = ttk.Label(frame, text="Enter a:")
label_a.grid(row=0, column=0, sticky=tk.W)
entry_a = ttk.Entry(frame)
entry_a.grid(row=0, column=1, sticky=tk.E)

label_b = ttk.Label(frame, text="Enter b:")
label_b.grid(row=1, column=0, sticky=tk.W)
entry_b = ttk.Entry(frame)
entry_b.grid(row=1, column=1, sticky=tk.E)

label_step = ttk.Label(frame, text="Enter step size:")
label_step.grid(row=2, column=0, sticky=tk.W)
entry_step = ttk.Entry(frame)
entry_step.grid(row=2, column=1, sticky=tk.E)

# Tabulate button
calculate_button = ttk.Button(frame, text="Tabulate", command=tabulate_function)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_text = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result_text)
result_label.grid(row=4, column=0, columnspan=2)

# Text area for tabulation results
text_output = tk.Text(frame, height=10, width=50)
text_output.grid(row=6, column=0, columnspan=2, pady=10)

window.mainloop()
