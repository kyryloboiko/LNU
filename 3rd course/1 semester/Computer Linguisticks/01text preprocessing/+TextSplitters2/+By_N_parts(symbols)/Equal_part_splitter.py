import os
from tkinter import Tk, simpledialog, messagebox
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


def split_text_into_parts(text, n_parts):
    parts_list = []
    part_size = len(text) / n_parts
    prev_cut = 0
    for i in range(n_parts):
        cut_text = text[prev_cut:int(prev_cut + part_size)]
        cut_text = " ".join(cut_text.split(" ")[0:-1])
        prev_cut += len(cut_text)
        parts_list.append(cut_text)

    parts_list[-1] += text[prev_cut:]

    for i, part in enumerate(parts_list, start=1):
        print(f"Part {i} length: {len(part)}")
    return parts_list


def write_part_to_file(index, part, full_path):
    filename = f'{index:02d}.txt'
    with open(os.path.join(full_path, filename), 'w', encoding='utf-8') as part_to_write:
        part_to_write.write(part)


def write_parts_to_files(parts_list, full_path):
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(write_part_to_file, i + 1, part, full_path)
                   for i, part in enumerate(parts_list, start=0)]

        # Wait for all tasks to complete
        for future in futures:
            future.result()


def main():
    root = Tk()
    root.withdraw()
    root.filename = askopenfilename(
        initialdir="/",
        title="Select file",
        filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    n_parts = simpledialog.askinteger(
        title="Split window",
        prompt="Введіть кількість частин",
        initialvalue=63)

    with open(root.filename, "r", encoding='utf-8') as file:
        text = file.read()

    # Remove script and style tags from HTML
    soup = BeautifulSoup(text, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()

    # Tokenize and split text
    parts_list = split_text_into_parts(text, n_parts)

    # User input for the save directory
    save_title = simpledialog.askstring(
        title="Save window",
        prompt="Введіть назву папки зберігання",
        initialvalue="Equal")
    full_path = os.path.join(os.path.dirname(root.filename), save_title)

    # Create the directory if it doesn't exist and write parts to files
    os.makedirs(full_path, exist_ok=True)
    write_parts_to_files(parts_list, full_path)

    messagebox.showinfo("Information", "Готово!")


if __name__ == '__main__':
    main()
