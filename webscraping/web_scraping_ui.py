import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup

class WebScrapingUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraping - Link Extractor")
        self.url_var = tk.StringVar(value="https://www.clcoding.com/")
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        url_label = ttk.Label(frame, text="URL:")
        url_label.grid(row=0, column=0, sticky=tk.W)
        url_entry = ttk.Entry(frame, textvariable=self.url_var, width=50)
        url_entry.grid(row=0, column=1, padx=5)

        scrape_btn = ttk.Button(frame, text="Get Links", command=self.scrape_links)
        scrape_btn.grid(row=0, column=2, padx=5)

        self.links_listbox = tk.Listbox(frame, width=80, height=20)
        self.links_listbox.grid(row=1, column=0, columnspan=3, pady=10)

    def scrape_links(self):
        url = self.url_var.get().strip()
        self.links_listbox.delete(0, tk.END)
        if not url:
            messagebox.showwarning("Warning", "Please enter a URL.")
            return
        try:
            r = requests.get(url, timeout=10)
            soup = BeautifulSoup(r.content, 'html.parser')
            links = soup.find_all('a')
            count = 0
            for link in links:
                href = link.get('href')
                if href:
                    self.links_listbox.insert(tk.END, href)
                    count += 1
            if count == 0:
                self.links_listbox.insert(tk.END, "No links found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to scrape: {e}")

if __name__ == '__main__':
    root = tk.Tk()
    app = WebScrapingUI(root)
    root.mainloop() 