import tkinter as tk
from tkinter import ttk
import random

class MinElementFinder:
    def __init__(self, master):
        self.master = master
        master.title("Find Minimum Element in Array")

        self.array_label = ttk.Label(master, text="Array (comma separated):")
        self.array_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.array_entry = ttk.Entry(master, width=30)
        self.array_entry.grid(row=0, column=1, padx=5, pady=5)

        self.random_array_button = ttk.Button(master, text="Generate Random Array", command=self.generate_random_array)
        self.random_array_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.find_button = ttk.Button(master, text="Find Minimum Element", command=self.find_min_element)
        self.find_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = ttk.Label(master, text="Result:")
        self.result_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        self.result_text = tk.Text(master, height=3, width=30)
        self.result_text.grid(row=3, column=1, padx=5, pady=5)
        self.result_text.config(state=tk.DISABLED)

    def generate_random_array(self, size=10, min_val=1, max_val=100):
        random_array = [random.randint(min_val, max_val) for _ in range(size)]
        self.array_entry.delete(0, tk.END)
        self.array_entry.insert(0, ','.join(map(str, random_array)))

    def find_min_element(self):
        try:
            array_str = self.array_entry.get()
            array = [int(x) for x in array_str.split(',')]

            if not array:
                self.display_result("Error: Array is empty.")
                return

            min_element = min(array)
            min_index = array.index(min_element)

            result_string = f"Minimum element: {min_element}\nIndex: {min_index}"
            self.display_result(result_string)

        except ValueError:
            self.display_result("Error: Invalid input. Please enter comma-separated numbers.")

    def display_result(self, result):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.config(state=tk.DISABLED)

root = tk.Tk()
app = MinElementFinder(root)
root.mainloop()