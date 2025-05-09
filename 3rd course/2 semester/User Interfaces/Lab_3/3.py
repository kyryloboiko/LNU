import tkinter as tk
import tkinter.messagebox as mb
import random

class MinElementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Пошук мінімального елемента в масиві")
        self.geometry("400x550")  # Increased height to accommodate the new input field
        self.resizable(False, False)

        self.var_array_size = tk.StringVar(value="10")
        self.var_manual_array = tk.StringVar()  # For manual array input
        self.array = []

        self.setup_ui()

    def setup_ui(self):
        wrapper = tk.Frame(self, bg="#e0f7fa")  # Light cyan
        wrapper.pack(fill="both", expand=True, padx=20, pady=14)

        input_frame = tk.Frame(wrapper, bg="#b2ebf2")  # Lighter cyan
        input_frame.pack(fill="x", pady=(0, 10), padx=10)

        size_label = tk.Label(input_frame, text="Розмір масиву:", font=("Segoe UI", 13, "bold"), fg="#00796b", bg="#b2ebf2")  # Dark teal
        size_label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))
        size_entry = tk.Entry(input_frame, textvariable=self.var_array_size, font=("Consolas", 13), width=10)
        size_entry.grid(row=1, column=0, padx=10, pady=(0, 10))

        # Manual array input
        manual_input_label = tk.Label(input_frame, text="Введіть масив (через кому або пробіл):", font=("Segoe UI", 13, "bold"), fg="#00796b", bg="#b2ebf2")
        manual_input_label.grid(row=2, column=0, sticky="w", padx=10, pady=(10, 2))
        manual_input_entry = tk.Entry(input_frame, textvariable=self.var_manual_array, font=("Consolas", 13), width=30)
        manual_input_entry.grid(row=3, column=0, padx=10, pady=(0, 10))

        btn_frame = tk.Frame(wrapper, bg="#e0f7fa")  # Light cyan
        btn_frame.pack(pady=(0, 10))

        tk.Button(btn_frame, text="Згенерувати масив", command=self.generate_array,
                      fg="#fff", bg="#4db6ac", activebackground="#26a69a",  # Teal
                      width=15, height=2).grid(row=0, column=0, padx=10, pady=8)

        tk.Button(btn_frame, text="Знайти мінімум", command=self.find_min,
                      fg="#fff", bg="#4db6ac", activebackground="#26a69a",  # Teal
                      width=15, height=2).grid(row=0, column=1, padx=10, pady=8)
        
        tk.Button(btn_frame, text="Ввести масив", command=self.enter_array,
                      fg="#fff", bg="#4db6ac", activebackground="#26a69a",  # Teal
                      width=15, height=2).grid(row=1, column=0, padx=10, pady=8)

        self.array_label = tk.Label(wrapper, text="Масив: []", font=("Segoe UI", 12), fg="#00695c", bg="#e0f7fa")  # Darker teal
        self.array_label.pack()

        self.result_label = tk.Label(wrapper, text="", font=("Segoe UI", 14, "bold"), fg="#00695c", bg="#e0f7fa")  # Darker teal
        self.result_label.pack()

    def generate_array(self):
        try:
            size = int(self.var_array_size.get())
            if size <= 0:
                raise ValueError("Розмір масиву повинен бути більше 0")

            self.array = [random.randint(1, 100) for _ in range(size)]
            self.array_label.config(text=f"Масив: {self.array}")
            self.result_label.config(text="")

        except ValueError as e:
            mb.showerror("Помилка", str(e))
            
    def enter_array(self):
        try:
            input_str = self.var_manual_array.get()
            if not input_str:
                raise ValueError("Будь ласка, введіть масив.")
            
            # Split the string by comma or space
            values = input_str.replace(",", " ").split()
            self.array = [int(val) for val in values]
            
            self.array_label.config(text=f"Масив: {self.array}")
            self.result_label.config(text="")
            
        except ValueError as e:
            mb.showerror("Помилка", "Невірний формат масиву. Введіть числа через кому або пробіл.")

    def find_min(self):
        if not self.array:
            mb.showinfo("Інформація", "Спочатку згенеруйте або введіть масив.")
            return

        min_val = min(self.array)
        min_index = self.array.index(min_val)
        self.result_label.config(text=f"Мінімальний елемент: {min_val}, індекс: {min_index}")

if __name__ == "__main__":
    app = MinElementApp()
    app.mainloop()
