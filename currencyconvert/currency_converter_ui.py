import tkinter as tk
from tkinter import ttk
import requests

API_KEY = "u6fFRPz7Rx5WnNWZWf11V1yU5rq8ItHB"

LANGS = {
    'vi': {
        'title': 'Chuyển đổi tiền tệ',
        'amount': 'Số tiền:',
        'from': 'Từ:',
        'to': 'Sang:',
        'convert': 'Chuyển đổi',
        'result': 'Kết quả:',
        'lang': 'Ngôn ngữ',
        'en': 'Tiếng Anh',
        'vi': 'Tiếng Việt',
        'error': 'Lỗi chuyển đổi!'
    },
    'en': {
        'title': 'Currency Converter',
        'amount': 'Amount:',
        'from': 'From:',
        'to': 'To:',
        'convert': 'Convert',
        'result': 'Result:',
        'lang': 'Language',
        'en': 'English',
        'vi': 'Vietnamese',
        'error': 'Conversion error!'
    }
}

CURRENCIES = ['USD', 'EUR', 'INR', 'JPY', 'GBP', 'CNY', 'VND']

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {"apikey": API_KEY}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        if data.get("success"):
            return data["result"]
        else:
            return None
    except Exception:
        return None

class CurrencyUI:
    def __init__(self, root):
        self.lang = 'vi'
        self.root = root
        self.root.title(LANGS[self.lang]['title'])
        self.amount_var = tk.StringVar(value='1')
        self.from_var = tk.StringVar(value='USD')
        self.to_var = tk.StringVar(value='VND')
        self.result_var = tk.StringVar()
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

        self.amount_frame = ttk.Frame(self.root)
        self.amount_frame.pack(pady=5)
        self.amount_label = ttk.Label(self.amount_frame)
        self.amount_label.pack(side=tk.LEFT)
        self.amount_entry = ttk.Entry(self.amount_frame, textvariable=self.amount_var, width=10)
        self.amount_entry.pack(side=tk.LEFT, padx=5)

        self.from_frame = ttk.Frame(self.root)
        self.from_frame.pack(pady=5)
        self.from_label = ttk.Label(self.from_frame)
        self.from_label.pack(side=tk.LEFT)
        self.from_combo = ttk.Combobox(self.from_frame, values=CURRENCIES, textvariable=self.from_var, state='readonly', width=7)
        self.from_combo.pack(side=tk.LEFT, padx=5)

        self.to_frame = ttk.Frame(self.root)
        self.to_frame.pack(pady=5)
        self.to_label = ttk.Label(self.to_frame)
        self.to_label.pack(side=tk.LEFT)
        self.to_combo = ttk.Combobox(self.to_frame, values=CURRENCIES, textvariable=self.to_var, state='readonly', width=7)
        self.to_combo.pack(side=tk.LEFT, padx=5)

        self.convert_btn = ttk.Button(self.root, command=self.convert)
        self.convert_btn.pack(pady=5)

        self.result_label = ttk.Label(self.root)
        self.result_label.pack(pady=5)
        self.result_display = ttk.Entry(self.root, textvariable=self.result_var, state='readonly', width=30)
        self.result_display.pack(pady=5)

    def update_language(self):
        lang_dict = LANGS['en'] if self.lang == 'en' else LANGS['vi']
        self.root.title(lang_dict['title'])
        self.amount_label.config(text=lang_dict['amount'])
        self.from_label.config(text=lang_dict['from'])
        self.to_label.config(text=lang_dict['to'])
        self.convert_btn.config(text=lang_dict['convert'])
        self.result_label.config(text=lang_dict['result'])
        self.lang_label.config(text=lang_dict['lang']+':')
        self.lang_combo.set(lang_dict['en'] if self.lang == 'en' else lang_dict['vi'])

    def change_language(self, event=None):
        selected = self.lang_combo.get()
        self.lang = 'en' if selected == 'English' else 'vi'
        self.update_language()

    def convert(self):
        try:
            amount = float(self.amount_var.get())
            from_cur = self.from_var.get()
            to_cur = self.to_var.get()
            result = convert_currency(amount, from_cur, to_cur)
            if result is not None:
                self.result_var.set(f"{amount} {from_cur} = {result:.4f} {to_cur}")
            else:
                self.result_var.set(LANGS[self.lang]['error'])
        except Exception:
            self.result_var.set(LANGS[self.lang]['error'])

if __name__ == '__main__':
    root = tk.Tk()
    app = CurrencyUI(root)
    root.mainloop() 