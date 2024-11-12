import re
import os
from tkinter import messagebox, Tk, simpledialog
from tkinter.filedialog import askopenfilename
from concurrent.futures import ThreadPoolExecutor


def save_file(args):
    part, index, save_path = args
    filename = f'{index:02d}.txt'
    with open(os.path.join(save_path, filename), 'w', encoding='utf-8') as part_to_write:
        part_to_write.write(part)


def main():
    root = Tk()
    root.withdraw()

    file_path = askopenfilename(
        initialdir="/",
        title="Select file",
        filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    pattern = simpledialog.askstring(
        title="Split window",
        prompt="Введіть розділювальне слово",
        initialvalue="chapter")

    with open(file_path, "r", encoding='utf-8') as file:
        text = file.read()

    # remove from text all /n /t /r
    text = re.sub(r'\s+', ' ', text)

    # Compile the regular expression outside the loop
    compiled_pattern = re.compile(pattern)
    parts_list = compiled_pattern.split(text)

    # add pattern to the end of each part
    for i in range(len(parts_list) - 1):
        parts_list[i] += pattern

    save_title = simpledialog.askstring(
        title="Save window",
        prompt="Введіть назву папки зберігання",
        initialvalue="Separated text")
    save_path = os.path.join(os.path.dirname(file_path), save_title)
    os.makedirs(save_path, exist_ok=True)

    # Use ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor() as executor:
        # Use list comprehension for file writing
        executor.map(
            save_file,
            [(part, index, save_path) for index, part in enumerate(parts_list, start=1)])

    messagebox.showinfo("Information", "Готово!")


if __name__ == '__main__':
    main()
