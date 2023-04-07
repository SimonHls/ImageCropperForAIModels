# Image cropper to generate 512x512 pixel images to train AI models.
# Simply put your images into a folder called "rawImages" and run the script in the enclosing folder.
# Written by AI (GPT-4) with only minor manual changes to legacy pillow functions, so free to use for anything with no license.

import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageCropper:

    def __init__(self, master):
        self.master = master
        self.master.title("Image Cropper")
        self.canvas = tk.Canvas(self.master, width=1600, height=1200) # Change canvas dimensions here and in line 54
        self.canvas.pack()

        self.raw_images_path = "rawImages"
        self.cropped_images_path = "croppedImages"

        # Generate croppedImages subfolder if it doesnt exist.
        if not os.path.exists(self.cropped_images_path):
            os.makedirs(self.cropped_images_path)

        self.files = os.listdir(self.raw_images_path)
        self.current_file_index = 0

        self.rect = None
        self.start_x = None
        self.start_y = None

        self.load_image()
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)
        self.master.bind("<Return>", self.on_enter)

    def resize_image(self, image, max_width, max_height):
        width, height = image.size
        aspect_ratio = float(width) / float(height)

        if width > max_width:
            width = max_width
            height = int(width / aspect_ratio)

        if height > max_height:
            height = max_height
            width = int(height * aspect_ratio)

        return image.resize((width, height), Image.Resampling.LANCZOS)

    def load_image(self):
        image_path = os.path.join(self.raw_images_path, self.files[self.current_file_index])
        self.image = Image.open(image_path)
        self.image = self.resize_image(self.image, 1600, 1200)
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)

    def on_mouse_down(self, event):
        if self.rect:
            self.canvas.delete(self.rect)

        self.start_x = event.x
        self.start_y = event.y

    def on_mouse_move(self, event):
        if self.rect:
            self.canvas.delete(self.rect)

        end_x = event.x
        end_y = self.start_y + (end_x - self.start_x) * (512 / 512)

        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, end_x, end_y, outline="red")

    # crop resize save
    def on_enter(self, event):
        if self.rect:
            x1, y1, x2, y2 = self.canvas.coords(self.rect)
            cropped_image = self.image.crop((x1, y1, x2, y2)).resize((512, 512), Image.Resampling.LANCZOS)
            cropped_image.save(os.path.join(self.cropped_images_path, f"cropped_{self.files[self.current_file_index]}"))

        self.current_file_index += 1
        if self.current_file_index < len(self.files):
            self.load_image()
        else:
            self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCropper(root)
    root.mainloop()
