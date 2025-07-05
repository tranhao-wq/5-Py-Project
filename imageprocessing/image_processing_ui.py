import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter
import os

class ImageProcessingUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing")
        self.img = None
        self.img_path = None
        self.tk_img = None
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        open_btn = ttk.Button(frame, text="Open Image", command=self.open_image)
        open_btn.grid(row=0, column=0, pady=5)

        self.img_label = ttk.Label(frame)
        self.img_label.grid(row=1, column=0, columnspan=4, pady=5)

        blur_btn = ttk.Button(frame, text="Blur", command=self.blur_image)
        blur_btn.grid(row=2, column=0, padx=5)
        gray_btn = ttk.Button(frame, text="Grayscale", command=self.gray_image)
        gray_btn.grid(row=2, column=1, padx=5)
        edge_btn = ttk.Button(frame, text="Find Edges", command=self.edge_image)
        edge_btn.grid(row=2, column=2, padx=5)
        reset_btn = ttk.Button(frame, text="Reset", command=self.show_image)
        reset_btn.grid(row=2, column=3, padx=5)

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if file_path:
            try:
                self.img = Image.open(file_path)
                self.img_path = file_path
                self.show_image()
            except Exception as e:
                messagebox.showerror("Error", f"Cannot open image: {e}")

    def show_image(self, img=None):
        if img is None:
            img = self.img
        if img is not None:
            img_disp = img.copy().resize((300, 300))
            self.tk_img = ImageTk.PhotoImage(img_disp)
            self.img_label.config(image=self.tk_img)
            self.img_label.image = self.tk_img

    def blur_image(self):
        if self.img:
            blur_img = self.img.filter(ImageFilter.BLUR)
            self.show_image(blur_img)

    def gray_image(self):
        if self.img:
            gray_img = self.img.convert('L').convert('RGB')
            self.show_image(gray_img)

    def edge_image(self):
        if self.img:
            edge_img = self.img.filter(ImageFilter.FIND_EDGES)
            self.show_image(edge_img)

if __name__ == '__main__':
    root = tk.Tk()
    app = ImageProcessingUI(root)
    root.mainloop() 