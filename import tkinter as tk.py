import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, master):
        self.master = master
        master.title("Watermark App")

        # Create UI elements
        self.upload_button = tk.Button(master, text="Upload Image", command=self.upload_image)
        self.watermark_entry = tk.Entry(master)
        self.apply_button = tk.Button(master, text="Apply Watermark", command=self.apply_watermark)
        self.preview_label = tk.Label(master)

        # Add UI elements to window
        self.upload_button.pack()
        self.watermark_entry.pack()
        self.apply_button.pack()
        self.preview_label.pack()

        # Initialize variables
        self.image = None
        self.watermark_text = ""

    def upload_image(self):
        # Open a file dialog to select an image file
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])

        # Load the selected image into memory and display a preview
        self.image = Image.open(file_path)
        self.image.thumbnail((300, 300))
        preview_image = Imagetk.PhotoImage(self.image)
        self.preview_label.configure(image=preview_image)
        self.preview_label.image = preview_image

    def apply_watermark(self):
        if self.image is not None:
            # Get the watermark text from the entry field
            self.watermark_text = self.watermark_entry.get()

            # Apply the watermark to the image
            draw = ImageDraw.Draw(self.image)
            font = ImageFont.truetype("arial.ttf", 50)
            text_width, text_height = draw.textsize(self.watermark_text, font)
            x = self.image.width - text_width - 10
            y = self.image.height - text_height - 10
            draw.text((x, y), self.watermark_text, font=font, fill=(255, 255, 255, 128))

            # Display the watermarked image
            preview_image = ImageTk.PhotoImage(self.image)
            self.preview_label.configure(image=preview_image)
            self.preview_label.image = preview_image

            # Save the watermarked image to a file
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg;*.jpeg")])
            self.image.save(save_path)

# Create a new window and start the app
root = tk.Tk()
app = WatermarkApp(root)
root.mainloop()
