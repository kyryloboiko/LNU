import customtkinter as ctk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import tkinter as tk
import math
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tipwindow:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + self.widget.winfo_rooty() + 20
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "10", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self, event=None):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

class FunctionTabulatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("💜 Інтерактивна табуляція функції")
        self.geometry("820x680")
        self.resizable(False, False)

        try:
            self.iconbitmap("icon.ico")
        except:
            pass

        self.var_a = ctk.DoubleVar(value=0.0)
        self.var_b = ctk.DoubleVar(value=1.0)
        self.var_n = ctk.IntVar(value=10)
        self.var_fx = ctk.StringVar(value="x + math.sqrt(x) + x**(1/3) - 2.5")

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Зберегти CSV", command=self.export_csv)
        file_menu.add_separator()
        file_menu.add_command(label="Вихід", command=self.destroy)
        menubar.add_cascade(label="Файл", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Про програму", command=lambda: mb.showinfo("Про програму", "Лабораторна робота №2. Табуляція функції з графіком."))
        menubar.add_cascade(label="Довідка", menu=help_menu)
        self.config(menu=menubar)

    def apply_template(self, selected):
        self.var_fx.set(selected)

    def create_widgets(self):
        main_frame = ctk.CTkFrame(self, fg_color="#f6f3ff")
        main_frame.pack(fill="both", expand=True, padx=16, pady=12)

        top_frame = ctk.CTkFrame(main_frame, fg_color="#eadfff")
        top_frame.pack(fill="x", padx=10, pady=(0, 8))

        fx_frame = ctk.CTkFrame(top_frame, fg_color="#efeaff")
        fx_frame.grid(row=0, column=0, padx=(10, 20), pady=10, sticky="n")
        ctk.CTkLabel(fx_frame, text="Функція f(x):", text_color="#673ab7", font=("Segoe UI", 13, "bold")).pack(anchor="w")
        self.fx_entry = ctk.CTkEntry(fx_frame, textvariable=self.var_fx, width=360, font=("Segoe UI", 13))
        self.fx_entry.pack()
        ToolTip(self.fx_entry, "Введіть функцію у вигляді Python (наприклад: x + math.sqrt(x))")

        ctk.CTkLabel(fx_frame, text="Шаблони функцій:", text_color="#673ab7", font=("Segoe UI", 12, "bold")).pack(pady=(10, 0))
        self.template_combo = ctk.CTkComboBox(fx_frame, values=[
            "x + math.sqrt(x) + x**(1/3) - 2.5",
            "x**2 - math.sin(x)",
            "math.log(x) + x",
            "np.exp(-x**2)"
        ], font=("Segoe UI", 12), width=260, command=self.apply_template)
        self.template_combo.set("Виберіть функцію…")
        self.template_combo.pack(pady=4)

        param_frame = ctk.CTkFrame(top_frame, fg_color="#efeaff")
        param_frame.grid(row=0, column=1, pady=10)
        self.add_slider(param_frame, "Початок діапазону a:", self.var_a, 0, 10, 0)
        self.add_slider(param_frame, "Кінець діапазону b:", self.var_b, 0.1, 20, 1)
        self.add_slider(param_frame, "Кількість точок N:", self.var_n, 2, 100, 2, True)

        self.stats_label = ctk.CTkLabel(main_frame, text="", font=("Segoe UI", 13, "bold"), text_color="#382874")
        self.stats_label.pack(pady=(4, 0))

        self.table_box = ctk.CTkTextbox(main_frame, height=160, font=("Consolas", 14, "bold"), fg_color="#f7f6fb", text_color="#2f2c57")
        self.table_box.pack(fill="both", padx=10, pady=6)

        plot_frame = ctk.CTkFrame(main_frame, height=200, fg_color="#efeaff")
        plot_frame.pack(fill="x", padx=10, pady=(0, 4))
        self.figure = plt.Figure(figsize=(6.2, 2.5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=plot_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        btn_frame = ctk.CTkFrame(main_frame, fg_color="#f2eaff")
        btn_frame.pack(side="bottom", fill="x", padx=10, pady=10)
        btn_frame.grid_columnconfigure((0, 1, 2), weight=1)

        tab_btn = ctk.CTkButton(btn_frame, text="📊 Табулювати", command=self.tabulate,
                                fg_color="#a259ff", hover_color="#873de4",
                                width=140, height=36)
        tab_btn.grid(row=0, column=0, padx=10, pady=5)
        ToolTip(tab_btn, "Обчислити значення функції")

        clr_btn = ctk.CTkButton(btn_frame, text="🧹 Очистити", command=self.clear_all,
                                fg_color="#a259ff", hover_color="#873de4",
                                width=140, height=36)
        clr_btn.grid(row=0, column=1, padx=10, pady=5)
        ToolTip(clr_btn, "Очистити таблицю та графік")

        save_btn = ctk.CTkButton(btn_frame, text="💾 Зберегти CSV", command=self.export_csv,
                                 fg_color="#a259ff", hover_color="#873de4",
                                 width=140, height=36)
        save_btn.grid(row=0, column=2, padx=10, pady=5)
        ToolTip(save_btn, "Зберегти таблицю у CSV файл")

    def add_slider(self, parent, label, variable, frm, to, row, is_int=False):
        ctk.CTkLabel(parent, text=label, text_color="#673ab7", font=("Segoe UI", 12)).grid(row=row, column=0, sticky="e")
        ctk.CTkEntry(parent, textvariable=variable, width=80, font=("Segoe UI", 12)).grid(row=row, column=1, padx=5)
        steps = to - frm if is_int else int((to - frm) * 10)
        slider = ctk.CTkSlider(parent, variable=variable, from_=frm, to=to, number_of_steps=steps)
        slider.configure(progress_color="#a259ff", button_color="#a259ff")
        slider.grid(row=row, column=2, padx=5, pady=4)

    def tabulate(self):
        try:
            a = float(self.var_a.get())
            b = float(self.var_b.get())
            n = int(self.var_n.get())
            fx_text = self.var_fx.get()
            if n < 2:
                raise ValueError
            if a > b:
                a, b = b, a
        except Exception:
            mb.showerror("Помилка", "Перевірте введення параметрів.")
            return

        self.table_box.delete("0.0", "end")
        x_vals = np.linspace(a, b, n)
        y_vals = []

        try:
            for x in x_vals:
                y = eval(fx_text, {"x": x, "math": math, "np": np})
                y_vals.append(y)
                line = f"x = {x:>7.4f}     f(x) = {y:>10.6f}"
                centered = line.center(70)
                self.table_box.insert("end", centered + "\n")
        except Exception as e:
            mb.showerror("Помилка у функції", f"Неможливо обчислити f(x):\n{e}")
            return

        y_min, y_max = min(y_vals), max(y_vals)
        y_avg = sum(y_vals) / len(y_vals)
        self.stats_label.configure(text=f"🔻 Мінімум: {y_min:.4f}     🔺 Максимум: {y_max:.4f}     📊 Середнє: {y_avg:.4f}")

        self.ax.clear()
        self.ax.plot(x_vals, y_vals, marker='o', linestyle='-', color='#a264f5')
        self.ax.set_title("Графік функції", fontsize=12)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")
        self.ax.grid(True, linestyle='--', linewidth=0.6)
        self.ax.legend(["f(x)"])
        self.canvas.draw()

    def clear_all(self):
        self.table_box.delete("0.0", "end")
        self.stats_label.configure(text="")
        self.ax.clear()
        self.canvas.draw()

    def export_csv(self):
        path = fd.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not path:
            return
        with open(path, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["x", "f(x)"])
            for line in self.table_box.get("0.0", "end").splitlines():
                if line.strip():
                    parts = line.replace("x = ", "").replace("f(x) = ", "").split()
                    writer.writerow(parts)
        mb.showinfo("Експортовано", "Файл збережено успішно!")

if __name__ == "__main__":
    app = FunctionTabulatorApp()
    app.mainloop()
