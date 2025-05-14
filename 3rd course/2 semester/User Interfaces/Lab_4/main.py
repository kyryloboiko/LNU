import tkinter as tk
from tkinter import ttk
import datetime
import pytz
from babel.dates import format_date
import copy

class WorldTimeAppEnhanced:
    def __init__(self, root):
        self.root = root
        self.root.title("Світовий Час Компаньйон (Таблиця)")
        self.root.geometry("1000x400")

        self.locale = 'uk_UA'

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
        style.configure("Treeview", font=("Helvetica", 10), rowheight=35)
        style.map('Treeview', background=[('selected', '#0078D7')])

        self.timezones_data = [
            {"city": "Київ", "tz": "Europe/Kyiv", "country": "Україна"},
            {"city": "Лондон", "tz": "Europe/London", "country": "Велика Британія"},
            {"city": "Нью-Йорк", "tz": "America/New_York", "country": "США"},
            {"city": "Токіо", "tz": "Asia/Tokyo", "country": "Японія"},
            {"city": "Сідней", "tz": "Australia/Sydney", "country": "Австралія"},
            {"city": "Берлін", "tz": "Europe/Berlin", "country": "Німеччина"},
            {"city": "Дубай", "tz": "Asia/Dubai", "country": "ОАЕ"},
            {"city": "Чикаго", "tz": "America/Chicago", "country": "США (CDT)"},
            {"city": "Париж", "tz": "Europe/Paris", "country": "Франція"}
        ]

        self.buttons = {}

        self.create_widgets()
        self.update_time()

    def get_localized_day_month(self, dt_object):
        try:
            return format_date(dt_object.date(), format='EEE, d MMM', locale=self.locale)
        except Exception:
            return dt_object.strftime("%a, %d %b")

    def create_widgets(self):
        header_label = ttk.Label(self.root, text="Поточний час у містах світу:", font=("Helvetica", 14, "bold"))
        header_label.pack(pady=(10, 5))

        cols = ("move_buttons", "city_details", "current_time_val", "h_neg2", "h_neg1", "h_curr", "h_pos1", "h_pos2", "h_pos3")
        self.tree = ttk.Treeview(self.root, columns=cols, show="headings")

        self.tree.heading("move_buttons", text="Переміщення")
        self.tree.heading("city_details", text="Місто / Зона / Дата")
        self.tree.heading("current_time_val", text="Час")
        self.tree.heading("h_neg2", text="H-2")
        self.tree.heading("h_neg1", text="H-1")
        self.tree.heading("h_curr", text="Пот. год.")
        self.tree.heading("h_pos1", text="H+1")
        self.tree.heading("h_pos2", text="H+2")
        self.tree.heading("h_pos3", text="H+3")

        self.tree.column("move_buttons", width=80, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.column("city_details", width=230, anchor=tk.W, stretch=tk.NO)
        self.tree.column("current_time_val", width=90, anchor=tk.CENTER, stretch=tk.NO)

        hour_col_width = 65
        for col_name in ["h_neg2", "h_neg1", "h_curr", "h_pos1", "h_pos2", "h_pos3"]:
            self.tree.column(col_name, width=hour_col_width, anchor=tk.CENTER, stretch=tk.YES)

        self.tree.tag_configure('even', background='#B7B8EA')
        self.tree.tag_configure('odd', background='#B6DEEA')
        self.tree.tag_configure('header', background='white')

        style = ttk.Style()
        style.configure("Treeview.Heading", borderwidth=1, relief="solid")

        self.tree.pack(expand=True, fill="both", padx=10, pady=5)

        self.tree.tag_configure('current_hour_text', font=('Helvetica', 10, 'bold'), foreground='#00529B')

        self.status_label = ttk.Label(self.root, text="", font=("Helvetica", 8))
        self.status_label.pack(side="bottom", fill="x", padx=10, pady=(0, 5))

    def create_move_buttons(self, item_id):
        index = int(item_id.split("_")[1])
        up_button = tk.Button(self.tree, text="ᐱ", command=lambda i=index: self.move_row(i, -1), width=2, height=1)
        down_button = tk.Button(self.tree, text="ᐯ", command=lambda i=index: self.move_row(i, 1), width=2, height=1)
        self.buttons[item_id] = (up_button, down_button)
        return "ᐱ ᐯ"

    def move_row(self, index, direction):
        new_index = index + direction

        if 0 < new_index < len(self.timezones_data):
            self.timezones_data[index], self.timezones_data[new_index] = self.timezones_data[new_index], self.timezones_data[index]
            self.update_time()

    def get_time_details(self, tz_name, city_info):
        try:
            timezone = pytz.timezone(tz_name)
            now = datetime.datetime.now(timezone)

            time_str = now.strftime("%H:%M:%S")
            date_str_localized = self.get_localized_day_month(now)

            tz_abbrev = now.tzname()
            offset_seconds = now.utcoffset().total_seconds()
            offset_hours = int(offset_seconds // 3600)
            offset_sign = "+" if offset_hours >= 0 else "-"
            offset_str = f"{tz_abbrev} {offset_sign}{abs(offset_hours)}"

            city_display = f"{city_info['city']}, {city_info['country']}\n{offset_str} • {date_str_localized}"

            hour_slots = []
            for h_offset in range(-2, 4):
                dt_for_slot = now + datetime.timedelta(hours=h_offset)
                hour_12 = dt_for_slot.strftime("%I").lstrip('0')
                am_pm = dt_for_slot.strftime("%p").lower()
                hour_slots.append(f"{hour_12}{am_pm}")

            return city_display, time_str, hour_slots

        except pytz.exceptions.UnknownTimeZoneError:
            return f"{city_info['city']}\nНевід. час. пояс", "Н/Д", ["--"] * 6
        except Exception as e:
            print(f"Помилка отримання деталей часу для {tz_name}: {e}")
            return f"{city_info['city']}\nПомилка", "Помилка", ["XX"] * 6

    def update_time(self):
        for i, city_data in enumerate(self.timezones_data):
            city_display_details, current_time_str, hour_slots_values = self.get_time_details(city_data["tz"],
                                                                                                city_data)

            item_id = f"row_{i}"

            if i != 0:
                move_buttons_text = self.create_move_buttons(item_id)
            else:
                move_buttons_text = ""

            values_tuple = (
                move_buttons_text,
                city_display_details,
                current_time_str,
                hour_slots_values[0],
                hour_slots_values[1],
                hour_slots_values[2],
                hour_slots_values[3],
                hour_slots_values[4],
                hour_slots_values[5]
            )

            if i % 2 == 0 and i != 0:
                self.tree.insert("", "end", iid=f"row_{i}", values=values_tuple, tags=('even',))
            elif i == 0:
                self.tree.insert("", "end", iid=f"row_{i}", values=values_tuple, tags=('header',))
            else:
                self.tree.insert("", "end", iid=f"row_{i}", values=values_tuple, tags=('odd',))
            for button in self.buttons.values():
                button[0].destroy()
                button[1].destroy()
            self.buttons = {}

        kyiv_tz = pytz.timezone('Europe/Kyiv')
        now_kyiv = datetime.datetime.now(kyiv_tz)
        self.status_label.config(text=f"Дані оновлено: {now_kyiv.strftime('%d-%m-%Y %H:%M:%S %Z')}")

        self.root.after(1000, self.update_time)


if __name__ == "__main__":
    root = tk.Tk()
    try:
        format_date(datetime.datetime.now().date(), format='EEE', locale='uk_UA')
    except Exception as e:
        print(f"Попередження: українська локаль ('uk_UA') може бути не повністю доступна для Babel: {e}")
        print("Можливе використання стандартного форматування дати, якщо виникнуть проблеми.")

    app = WorldTimeAppEnhanced(root)
    root.mainloop()
