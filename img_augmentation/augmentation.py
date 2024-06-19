import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def select_directory(label):
    directory = filedialog.askdirectory()
    if directory:
        label.config(text=directory)

def augment_images(input_dir, output_dir, num_images, resize, rotate):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    images = []
    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(('jpg')):
            image_path = os.path.join(input_dir, file_name)
            image = Image.open(image_path)
            images.append(image)

    def apply_transformations(img, resize, rotate):
        if resize:
            width, height = img.size
            img = img.resize((int(width * resize), int(height * resize)))
        
        if rotate:
            img = img.rotate(rotate)
        
        return img

    for i in range(num_images):
        for img in images:
            transformed_image = apply_transformations(img, resize, rotate)
            output_path = os.path.join(output_dir, f"augmented_{i}")
            transformed_image.save(output_path)
    
    messagebox.showinfo("Done", "Images are saved")

def main():
    root = tk.Tk()
    root.title("Image augmentation")
    root.geometry("600x700")
    root.minsize(500, 750)

    #scroll_bar = tk.Scrollbar(root)
    #scroll_bar.pack(side="right", fill="y")

    input_label = tk.Label(root, text="Select the directory with images")
    input_label.pack(anchor="center")

    input_dir_label = tk.Label(root, text="", wraplength=500)
    input_dir_label.pack()

    input_dir_button = ttk.Button(root, text="Select the directory", command=lambda: select_directory(input_dir_label))
    input_dir_button.pack(pady=10)

    output_label = tk.Label(root, text="Select the directory to save images:")
    output_label.pack(pady=10)

    output_dir_label = tk.Label(root, text="", wraplength=500)
    output_dir_label.pack()

    output_dir_button = ttk.Button(root, text="Select the directory", command=lambda: select_directory(output_dir_label))
    output_dir_button.pack(pady=10)

    num_images_label = tk.Label(root, text="Enter the number of images to create")
    num_images_label.pack()

    num_images_entry = ttk.Entry(root)
    num_images_entry.pack(pady=10)

    resize_label = tk.Label(root, text="Scaling (from 0 to 1):")
    resize_label.pack()
    resize_entry = ttk.Entry(root)
    resize_entry.pack(pady=5)

    rotate_label = tk.Label(root, text="Rotation (degrees):")
    rotate_label.pack()
    rotate_entry = ttk.Entry(root)
    rotate_entry.pack(pady=5)

    augment_button = ttk.Button(root, text="Start augmentation", 
                                command=lambda: augment_images(
                                    input_dir_label.cget("text"), 
                                    output_dir_label.cget("text"), 
                                    num_images_entry.get(),
                                    float(resize_entry.get() or 1),
                                    int(rotate_entry.get() or 0)
                                ))
    augment_button.pack(pady=15)

    root.mainloop()

if __name__ == "__main__":
    main()