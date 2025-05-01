import customtkinter as ctk
import tkinter.messagebox as mb
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

class IntegralApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("💜 Обчислення інтегралу методом прямокутників")
        self.geometry("800x620")
        self.resizable(False, False)

        self.var_a = ctk.StringVar(value="0")
        self.var_b = ctk.StringVar(value="1")
        self.var_n = ctk.StringVar(value="10")
        self.var_fx = ctk.StringVar(value="math.sin(x)")

        self.setup_ui()

    def apply_template(self, selected):
        self.var_fx.set(selected)

    def setup_ui(self):
        wrapper = ctk.CTkFrame(self, fg_color="#f3efff")
        wrapper.pack(fill="both", expand=True, padx=20, pady=14)

        input_frame = ctk.CTkFrame(wrapper, fg_color="#e5dafc")
        input_frame.pack(fill="x", pady=(0, 10), padx=10)

        fx_label = ctk.CTkLabel(input_frame, text="Функція f(x):", font=("Segoe UI", 13, "bold"), text_color="#5e35b1")
        fx_label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))
        fx_entry = ctk.CTkEntry(input_frame, textvariable=self.var_fx, font=("Consolas", 13), width=300)
        fx_entry.grid(row=1, column=0, padx=10, pady=(0, 10))

        ctk.CTkLabel(input_frame, text="Шаблони функцій:", text_color="#5e35b1", font=("Segoe UI", 12, "bold")).grid(row=2, column=0, sticky="w", padx=10)
        self.template_combo = ctk.CTkComboBox(input_frame, values=[
            "math.sin(x)", "x**2", "math.exp(-x)", "math.sqrt(x)", "x + math.cos(x)"
        ], font=("Segoe UI", 12), width=250, command=self.apply_template)
        self.template_combo.set("Виберіть функцію…")
        self.template_combo.grid(row=3, column=0, padx=10, pady=(0, 10))

        param_frame = ctk.CTkFrame(input_frame, fg_color="#ece3ff")
        param_frame.grid(row=0, column=1, rowspan=4, padx=20, pady=10)

        self.add_input(param_frame, "Нижня межа a:", self.var_a, 0)
        self.add_input(param_frame, "Верхня межа b:", self.var_b, 1)
        self.add_input(param_frame, "Кількість прямокутників N:", self.var_n, 2)

        btn_frame = ctk.CTkFrame(wrapper, fg_color="#f3efff")
        btn_frame.pack(pady=(0, 10))

        ctk.CTkButton(btn_frame, text="📐 Обчислити", command=self.calculate,
                      fg_color="#a259ff", hover_color="#873de4",
                      width=140, height=36).grid(row=0, column=0, padx=10, pady=8)

        ctk.CTkButton(btn_frame, text="🧹 Очистити", command=self.clear,
                      fg_color="#a259ff", hover_color="#873de4",
                      width=140, height=36).grid(row=0, column=1, padx=10, pady=8)

        self.result_label = ctk.CTkLabel(wrapper, text="", font=("Segoe UI", 14, "bold"), text_color="#4a148c")
        self.result_label.pack()

        graph_frame = ctk.CTkFrame(wrapper, height=300, fg_color="#f0e8ff")
        graph_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.fig, self.ax = plt.subplots(figsize=(6.8, 2.8), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=graph_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def add_input(self, parent, label, var, row):
        ctk.CTkLabel(parent, text=label, font=("Segoe UI", 12), text_color="#5e35b1").grid(row=row, column=0, padx=10, pady=5, sticky="e")
        ctk.CTkEntry(parent, textvariable=var, font=("Segoe UI", 12), width=100).grid(row=row, column=1, padx=10)

    def calculate(self):
        try:
            a = float(self.var_a.get())
            b = float(self.var_b.get())
            n = int(self.var_n.get())
            fx = self.var_fx.get()

            if n <= 0 or a >= b:
                raise ValueError("Некоректні межі або N")

            dx = (b - a) / n
            x_vals = np.linspace(a, b, n + 1)
            y_vals = []

            result = 0
            for i in range(n):
                x = x_vals[i]
                y = eval(fx, {"x": x, "math": math, "np": np})
                y_vals.append(y)
                result += y * dx

            self.result_label.configure(text=f"📊 Результат інтегрування: {result:.6f}")
            self.animate_plot(x_vals, y_vals, dx, fx)
        except Exception as e:
            mb.showerror("Помилка", f"Невірні дані або помилка функції:\n{e}")

    def animate_plot(self, x_vals, y_vals, dx, fx_text):
        self.ax.clear()
        try:
            x_plot = np.linspace(float(self.var_a.get()), float(self.var_b.get()), 300)
            y_plot = [eval(fx_text, {"x": x, "math": math, "np": np}) for x in x_plot]
            self.ax.plot(x_plot, y_plot, color="#a259ff", label="f(x)")
            self.ax.fill_between(x_plot, y_plot, color="#dec1ff", alpha=0.3)
        except:
            pass

        # Поступове додавання прямокутників
        self.ax.set_title("Графік та прямокутники", fontsize=11)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")
        self.ax.grid(True, linestyle="--", linewidth=0.5)
        self.ax.legend()

        def draw_bar(i):
            if i >= len(y_vals):
                self.canvas.draw()
                return
            self.ax.bar(x_vals[i], y_vals[i], width=dx, align='edge',
                        alpha=0.3, color="#c085f5", edgecolor="purple")
            self.canvas.draw()
            self.after(30, lambda: draw_bar(i + 1))

        draw_bar(0)

    def clear(self):
        self.result_label.configure(text="")
        self.ax.clear()
        self.canvas.draw()

if __name__ == "__main__":
    app = IntegralApp()
    app.mainloop()
