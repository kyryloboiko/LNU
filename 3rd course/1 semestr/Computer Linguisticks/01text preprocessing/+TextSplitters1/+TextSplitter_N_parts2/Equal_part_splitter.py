import os.path
from tkinter import messagebox, Tk, simpledialog
from tkinter.filedialog import askopenfilename

import unicodedata, re, itertools, sys

all_chars = (chr(i) for i in range(sys.maxunicode))
categories = {'Cc'}
control_chars = ''.join(c for c in all_chars if unicodedata.category(c) in categories)
# or equivalently and much more efficiently
control_chars = ''.join(map(chr, itertools.chain(range(0x00,0x20), range(0x7f,0xa0))))

control_char_re = re.compile('[%s]' % re.escape(control_chars))

def remove_control_chars(s):
    return control_char_re.sub(' ', s)

def main(str_list, full_path):
    lich = 0
    names = [str(i) for i in range(10, len(str_list))]
    names2 = ["0"+str(i) for i in range(10)]
    names2 = names2 + names
    for part in parts_list:
        string = ''
        for word in part:
            string += word
        filename = names2[lich]
        with open(full_path + '\\' + filename + '.txt', 'w', encoding="utf-8") as part_to_write:
            part_to_write.write(string)  # write to file
        lich += 1

if __name__ == '__main__':
    root = Tk()
    root.filename = askopenfilename(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    n_parts = simpledialog.askinteger(title="Split window", prompt="Enter the number of parts", initialvalue="63")
    with open(root.filename, "r", encoding="utf-8") as file:
        text = file.read()


    # tokenizer = RegexpTokenizer(r'[\w]+')

    tok = remove_control_chars(text)

    l = int(len(tok) / n_parts)
    parts_list = list(map(''.join, zip(*[iter(tok)]*l)))

    file_name = os.path.splitext(os.path.basename(os.path.realpath(__file__)))[0]
    save_title = simpledialog.askstring(title="Save window", prompt="Enter the folder name for saving", initialvalue="Equal")
    full_path = os.path.join(os.getcwd(), save_title)
    if not os.path.exists(full_path):
        os.mkdir(full_path)
    main(parts_list, full_path)
    messagebox.showinfo("Information", "Done!")
