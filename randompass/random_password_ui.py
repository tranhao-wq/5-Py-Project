import tkinter as tk
from tkinter import ttk
import random
import string

LANGS = {
    'vi': {
        'title': 'Sinh mật khẩu ngẫu nhiên',
        'length': 'Độ dài:',
        'generate': 'Sinh mật khẩu',
        'result': 'Mật khẩu:',
        'lang': 'Ngôn ngữ',
        'en': 'Tiếng Anh',
        'vi': 'Tiếng Việt',
    },
    'en': {
        'title': 'Random Password Generator',
        'length': 'Length:',
        'generate': 'Generate Password',
        'result': 'Password:',
        'lang': 'Language',
        'en': 'English',
        'vi': 'Vietnamese',
    }
}

class PasswordUI:
    def __init__(self, root):
        self.lang = 'vi'
        self.root = root
        self.root.title(LANGS[self.lang]['title'])
        self.length_var = tk.IntVar(value=10)
        self.password_var = tk.StringVar()
        self.create_widgets()
        self.update_language()

    def create_widgets(self):
        self.lang_frame = ttk.Frame(self.root)
        self.lang_frame.pack(pady=5)
        self.lang_label = ttk.Label(self.lang_frame)
        self.lang_label.pack(side=tk.LEFT)
        self.lang_combo = ttk.Combobox(self.lang_frame, values=['English', 'Vietnamese'], state='readonly')
        self.lang_combo.current(1)
        self.lang_combo.pack(side=tk.LEFT, padx=5)
        self.lang_combo.bind('<<ComboboxSelected>>', self.change_language)

        self.length_frame = ttk.Frame(self.root)
        self.length_frame.pack(pady=5)
        self.length_label = ttk.Label(self.length_frame)
        self.length_label.pack(side=tk.LEFT)
        self.length_entry = ttk.Entry(self.length_frame, textvariable=self.length_var, width=5)
        self.length_entry.pack(side=tk.LEFT, padx=5)

        self.generate_btn = ttk.Button(self.root, command=self.generate_password)
        self.generate_btn.pack(pady=5)

        self.result_label = ttk.Label(self.root)
        self.result_label.pack(pady=5)
        self.password_display = ttk.Entry(self.root, textvariable=self.password_var, state='readonly', width=30)
        self.password_display.pack(pady=5)

    def update_language(self):
        lang_dict = LANGS['en'] if self.lang == 'en' else LANGS['vi']
        self.root.title(lang_dict['title'])
        self.length_label.config(text=lang_dict['length'])
        self.generate_btn.config(text=lang_dict['generate'])
        self.result_label.config(text=lang_dict['result'])
        self.lang_label.config(text=lang_dict['lang']+':')
        self.lang_combo.set(lang_dict['en'] if self.lang == 'en' else lang_dict['vi'])

    def change_language(self, event=None):
        selected = self.lang_combo.get()
        self.lang = 'en' if selected == 'English' else 'vi'
        self.update_language()

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length <= 0:
                self.password_var.set('')
                return
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            self.password_var.set(password)
        except Exception:
            self.password_var.set('')

if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordUI(root)
    root.mainloop() 