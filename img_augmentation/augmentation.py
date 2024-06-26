import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from PIL import Image
from image_processor import ImageProcessor

class ImageAugmentationApp:
    """
    A class to create a GUI application for image augmentation.

    Attributes
    ----------
    root : Tk
        The root window of the Tkinter application.
    processor : ImageProcessor
        An instance of ImageProcessor to handle image transformations.

    Methods
    -------
    setup_gui():
        Sets up the GUI components of the application.
    select_input_directory():
        Opens a dialog to select the input directory.
    select_output_directory():
        Opens a dialog to select the output directory.
    start_augmentation():
        Starts the image augmentation process based on user inputs.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Image Augmentation")
        self.root.geometry("500x650")
        self.root.minsize(500, 650)
        
        self.processor = ImageProcessor() 

        self.setup_gui()

    def setup_gui(self):
        """
        Sets up the GUI components of the application.
        """
        input_label = tk.Label(self.root, text="Select the directory with images")
        input_label.pack(anchor="center")

        self.input_dir_label = tk.Label(self.root, text="", wraplength=500)
        self.input_dir_label.pack()

        input_dir_button = ttk.Button(self.root, text="Select the directory", command=self.select_input_directory)
        input_dir_button.pack(pady=10)

        output_label = tk.Label(self.root, text="Select the directory to save images:")
        output_label.pack(pady=10)

        self.output_dir_label = tk.Label(self.root, text="", wraplength=500)
        self.output_dir_label.pack()

        output_dir_button = ttk.Button(self.root, text="Select the directory", command=self.select_output_directory)
        output_dir_button.pack(pady=10)

        num_images_label = tk.Label(self.root, text="Enter the number of images to create")
        num_images_label.pack()

        self.num_images_entry = ttk.Entry(self.root)
        self.num_images_entry.pack(pady=10)

        resize_label = tk.Label(self.root, text="Scaling (from 0 to 1):")
        resize_label.pack()
        self.resize_entry = ttk.Entry(self.root)
        self.resize_entry.pack(pady=5)

        rotate_label = tk.Label(self.root, text="Rotation (degrees):")
        rotate_label.pack()
        self.rotate_entry = ttk.Entry(self.root)
        self.rotate_entry.pack(pady=5)

        brightness_label = tk.Label(self.root, text="Brightness (1.0 - the original image):")
        brightness_label.pack()
        self.brightness_entry = ttk.Entry(self.root)
        self.brightness_entry.pack(pady=5)

        contrast_label = tk.Label(self.root, text="Contrast (1.0 - the original image):")
        contrast_label.pack()
        self.contrast_entry = ttk.Entry(self.root)
        self.contrast_entry.pack(pady=5)

        saturation_label = tk.Label(self.root, text="Saturation (1.0 - the original image):")
        saturation_label.pack()
        self.saturation_entry = ttk.Entry(self.root)
        self.saturation_entry.pack(pady=5)

        augment_button = ttk.Button(self.root, text="Start augmentation", command=self.start_augmentation)
        augment_button.pack(pady=15)

    def select_input_directory(self):
        """
        Opens a dialog to select the input directory.
        """
        directory = filedialog.askdirectory()
        if directory:
            self.input_dir_label.config(text=directory)

    def select_output_directory(self):
        """
        Opens a dialog to select the output directory.
        """
        directory = filedialog.askdirectory()
        if directory:
            self.output_dir_label.config(text=directory)

    def start_augmentation(self):
        """
        Starts the image augmentation process based on user inputs.
        """
        input_dir = self.input_dir_label.cget("text")
        output_dir = self.output_dir_label.cget("text")
        num_images = self.num_images_entry.get()
        resize = float(self.resize_entry.get() or 1)
        rotate = int(self.rotate_entry.get() or 0)
        brightness_factor = float(self.brightness_entry.get() or 1.0)
        contrast_factor = float(self.contrast_entry.get() or 1.0)
        saturation_factor = float(self.saturation_entry.get() or 1.0)

        def show_error(message):
            """
            Displays an error message.

            Parameters
            ----------
            message : str
                The error message to display.
            """
            messagebox.showerror("Error", message)

        if not input_dir or not output_dir or not num_images:
            show_error("Fill in all the fields")
            return

        try:
            num_images = int(num_images)
            if num_images <= 0:
                raise ValueError
        except ValueError:
            show_error("Number of images must be positive")
            return

        try:
            resize = float(resize)
            if not (0 <= resize <= 1):
                raise ValueError
        except ValueError:
            show_error("Resize value must be in range of 0 to 1")
            return

        try:
            rotate = float(rotate)
        except ValueError:
            show_error("Rotation must be a number")
            return

        self.processor.set_brightness(brightness_factor)
        self.processor.set_contrast(contrast_factor)
        self.processor.set_saturation(saturation_factor)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        images = []
        for file_name in os.listdir(input_dir):
            if file_name.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):
                image_path = os.path.join(input_dir, file_name)
                image = Image.open(image_path)
                images.append(image)

        for i in range(num_images):
            for img in images:
                transformed_image = self.processor.apply_transformations(img, resize, rotate)
                output_path = os.path.join(output_dir, f"augmented_{i}_{os.path.basename(img.filename)}")
                transformed_image.save(output_path)

        messagebox.showinfo("Done", "Images are saved")