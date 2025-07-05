import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
import os

class QRCodeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.data_var = tk.StringVar()
        self.qr_img = None
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        label = ttk.Label(frame, text="Enter data/URL:")
        label.grid(row=0, column=0, sticky=tk.W)
        entry = ttk.Entry(frame, textvariable=self.data_var, width=40)
        entry.grid(row=0, column=1, padx=5)

        gen_btn = ttk.Button(frame, text="Generate QR", command=self.generate_qr)
        gen_btn.grid(row=1, column=0, columnspan=2, pady=5)

        self.qr_label = ttk.Label(frame)
        self.qr_label.grid(row=2, column=0, columnspan=2, pady=5)

        save_btn = ttk.Button(frame, text="Save QR", command=self.save_qr)
        save_btn.grid(row=3, column=0, columnspan=2, pady=5)

    def generate_qr(self):
        data = self.data_var.get().strip()
        if not data:
            messagebox.showwarning("Warning", "Please enter data to generate QR code.")
            return
        img = qrcode.make(data)
        self.qr_img = img
        img_tk = ImageTk.PhotoImage(img.resize((200, 200)))
        self.qr_label.configure(image=img_tk)
        self.qr_label.image = img_tk

    def save_qr(self):
        if self.qr_img is None:
            messagebox.showwarning("Warning", "No QR code to save. Please generate one first.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            try:
                self.qr_img.save(file_path)
                messagebox.showinfo("Success", f"QR code saved to {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save QR code: {e}")

if __name__ == '__main__':
    root = tk.Tk()
    app = QRCodeUI(root)
    root.mainloop() 