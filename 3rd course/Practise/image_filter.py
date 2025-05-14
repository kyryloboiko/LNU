import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk


class ImageFilterApp:
    def __init__(self, master):
        self.master = master
        master.title("Фільтрація зображень")

        self.image = None
        self.image_tk = None
        self.filtered_image = None
        self.filtered_image_tk = None

        self.open_button = tk.Button(master, text="Відкрити зображення", command=self.open_image)
        self.open_button.pack(pady=5)

        self.filter_frame = tk.Frame(master)
        self.filter_frame.pack()

        self.size_label = tk.Label(self.filter_frame, text="Розмір вікна:")
        self.size_label.grid(row=0, column=0)
        self.size_var = tk.IntVar(value=3)
        self.size_entry = tk.Entry(self.filter_frame, textvariable=self.size_var, width=5)
        self.size_entry.grid(row=0, column=1)

        self.filter_type_label = tk.Label(self.filter_frame, text="Тип фільтра:")
        self.filter_type_label.grid(row=1, column=0)
        self.filter_type_var = tk.StringVar(value="average")
        self.filter_type_menu = tk.OptionMenu(self.filter_frame, self.filter_type_var, "average", "median")
        self.filter_type_menu.grid(row=1, column=1)

        self.resize_label = tk.Label(self.filter_frame, text="Режим зміни розміру:")
        self.resize_label.grid(row=2, column=0)
        self.resize_var = tk.StringVar(value="unchanged")
        self.resize_menu = tk.OptionMenu(self.filter_frame, self.resize_var, "unchanged", "reduced")
        self.resize_menu.grid(row=2, column=1)

        self.apply_button = tk.Button(master, text="Застосувати фільтр", command=self.apply_filter)
        self.apply_button.pack(pady=5)

        self.canvas_original = tk.Canvas(master)
        self.canvas_original.pack(side=tk.LEFT)

        self.canvas_filtered = tk.Canvas(master)
        self.canvas_filtered.pack(side=tk.LEFT)

        self.save_button = tk.Button(master, text="Зберегти результат", command=self.save_image)
        self.save_button.pack(pady=5)

    def open_image(self):
        try:
            filepath = filedialog.askopenfilename(
                title="Виберіть зображення",
                filetypes=(("Зображення", "*.jpg;*.jpeg;*.png;*.bmp;*.gif;*.tiff"), ("Всі файли", "*.*"))
            )
            if filepath:
                self.image = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
                if self.image is None:
                    raise ValueError("Помилка завантаження зображення. Можливо, невірний формат файлу.")
                self.display_image()
        except Exception as e:
            messagebox.showerror("Помилка відкриття", str(e))

    def display_image(self):
        if self.image is not None:
            try:
                image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
                self.image_tk = ImageTk.PhotoImage(image=Image.fromarray(image_rgb))

                self.canvas_original.config(width=self.image_tk.width(), height=self.image_tk.height())
                self.canvas_original.create_image(0, 0, anchor=tk.NW, image=self.image_tk)

                self.canvas_filtered.delete("all")
                if self.filtered_image_tk is not None:
                    self.canvas_filtered.config(width=self.filtered_image_tk.width(), height=self.filtered_image_tk.height())
                    self.canvas_filtered.create_image(0, 0, anchor=tk.NW, image=self.filtered_image_tk)
            except Exception as e:
                messagebox.showerror("Помилка відображення", str(e))

    def apply_filter(self):
        if self.image is not None:
            try:
                r = int(self.size_entry.get())
                if r < 2:
                    raise ValueError("Розмір вікна повинен бути більше або дорівнювати 2")
                if r % 2 == 0 and self.filter_type_var.get() == "median":
                    raise ValueError("Розмір вікна для медіанного фільтра повинен бути непарним")

                filter_type = self.filter_type_var.get()
                resize_mode = self.resize_var.get()

                filtered_image = self.apply_filter_based_on_type(r, resize_mode, filter_type)

                filtered_image_rgb = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)
                self.filtered_image_tk = ImageTk.PhotoImage(image=Image.fromarray(filtered_image_rgb))
                self.display_image()

                self.filtered_image = filtered_image

            except cv2.error as e:
                messagebox.showerror("Помилка фільтрації", str(e))
            except Exception as e:
                messagebox.showerror("Помилка", str(e))

    def apply_filter_based_on_type(self, r, resize_mode, filter_type):
        try:
            if filter_type == "average":
                filtered_image = cv2.blur(self.image, (r, r))
            elif filter_type == "median":
                filtered_image = cv2.medianBlur(self.image, r)
            else:
                raise ValueError("Невідомий тип фільтра")

            if resize_mode == "reduced":
                h, w = filtered_image.shape[:2]
                new_h = h // r
                new_w = w // r
                filtered_image = cv2.resize(filtered_image, (new_w, new_h), interpolation=cv2.INTER_AREA)

            return filtered_image

        except Exception as e:
            messagebox.showerror(f"Помилка {filter_type} фільтрації", str(e))
            return self.image

    def save_image(self):
        if self.filtered_image is not None:
            try:
                filepath = filedialog.asksaveasfilename(
                    defaultextension=".png",
                    filetypes=(("PNG зображення", "*.png"), ("JPEG зображення", "*.jpg;*.jpeg"), ("Всі файли", "*.*")),
                    title="Зберегти зображення"
                )
                if filepath:
                    cv2.imwrite(filepath, self.filtered_image)
                    messagebox.showinfo("Збережено", "Зображення успішно збережено.")
            except Exception as e:
                messagebox.showerror("Помилка збереження", str(e))
        else:
            messagebox.showwarning("Увага", "Немає відфільтрованого зображення для збереження.")


root = tk.Tk()
app = ImageFilterApp(root)

def resize_widgets(event=None):
    size = 10
    try:
        scale_factor = root.winfo_pixels('1i') / 72
        size = int(10 * scale_factor)
    except Exception:
        pass
    for widget in root.winfo_children():
        try:
            widget.config(font=("Arial", size))
        except Exception:
            pass

root.bind("<Configure>", resize_widgets)
root.after(0, resize_widgets)

root.mainloop()
