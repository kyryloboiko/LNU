import os.path
from tkinter import messagebox, Tk, simpledialog
from tkinter.filedialog import askopenfilename

import unicodedata, re, itertools, sys


all_chars = (chr(i) for i in range(sys.maxunicode))
categories = {'Cc'}
control_chars = ''.join(c for c in all_chars if unicodedata.category(c) in categories)

control_chars = ''.join(map(chr, itertools.chain(range(0x00,0x20), range(0x7f,0xa0))))

control_char_re = re.compile('[%s]' % re.escape(control_chars))

def remove_control_chars(s):
    return control_char_re.sub(' ', s)

def main(parts_list):
    for index, part in enumerate(parts_list, start=1):
        if index < 10:
            filename = '\\0' + str(index)
        else:
            filename = '\\' + str(index)

        with open(full_path + filename + '.txt', 'w', encoding='utf-8') as part_to_write:
            part_to_write.write(part)


if __name__ == '__main__':
    root = Tk()
    root.filename = askopenfilename(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    pattern = simpledialog.askstring(title="Split window", prompt="Введіть розділювальне слово", initialvalue="chapter" )
    pattern = remove_control_chars(pattern)
    with open(root.filename, "r", encoding='utf-8') as file:
        text = file.read()

    text = remove_control_chars(text)
    parts_list = re.compile(pattern, flags=re.UNICODE).split(text)  # розділення тексту за ознакою pattern

    for i in range(len(parts_list) - 1):
        parts_list[i] = parts_list[i] + pattern

    file_name = os.path.splitext(os.path.basename(os.path.realpath(__file__)))[0]
    save_title = simpledialog.askstring(title="Save window", prompt="Веддіть назву папки зберігання", initialvalue="Separated text")
    full_path = os.path.join(os.getcwd(), save_title)
    if not os.path.exists(full_path):
        os.mkdir(full_path)
    main(parts_list)
    messagebox.showinfo("Information", "Готово!")
