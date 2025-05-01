import tkinter as tk
from tkinter import messagebox

def find_min_element_and_index():
    input_string = entry_array.get()

    if not input_string.strip():
        messagebox.showerror("Помилка", "Поле вводу порожнє. Введи числа.")
        label_result.config(text="Результат:")
        return

    try:
        processed_string = input_string.replace(',', ' ')
        elements = [item for item in processed_string.split() if item]

        if not elements:
             raise ValueError("Масив порожній після обробки.")

        numbers = [float(elem) for elem in elements]

    except ValueError:
        messagebox.showerror("Помилка вводу", "Будь ласка, вводь тільки числа, розділені пробілом або комою.")
        label_result.config(text="Результат: Неправильний ввід")
        return

    try:
        min_value = min(numbers)
        min_index = numbers.index(min_value)

        if min_value == int(min_value):
            min_value_str = str(int(min_value))
        else:
            min_value_str = str(min_value)

        result_text = f"Результат:\nНайменше число: {min_value_str}\nЙого індекс: {min_index}"
        label_result.config(text=result_text)

    except Exception as e:
        messagebox.showerror("Помилка обробки", f"Щось пішло не так: {e}")
        label_result.config(text="Результат: Помилка")

# Window
window = tk.Tk()
window.title("Пошук мінімуму в масиві")
window.geometry("450x250")

# Text
label_instruction = tk.Label(window, text="Введи числа через пробіл або кому:")
label_instruction.pack(pady=10)

# Input
entry_array = tk.Entry(window, width=50)
entry_array.pack(pady=5)

# Function's button
button_calculate = tk.Button(window, text="Знайти мінімум", command=find_min_element_and_index)
button_calculate.pack(pady=15)

# Result
label_result = tk.Label(window, text="Результат:", justify=tk.LEFT, font=("Arial", 11))
label_result.pack(pady=10)

window.mainloop()