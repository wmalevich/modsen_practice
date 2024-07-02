import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from PIL import Image, ImageTk
from img_augmentation.processor import ImageProcessor

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
        self.root.geometry("710x710")
        self.root.minsize(710, 710)
        
        self.setup_gui()

    def setup_gui(self):
        """
        Sets up the GUI components of the application.
        """
        left_frame = tk.Frame(self.root)
        left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        right_frame = tk.Frame(self.root)
        right_frame.pack(side=tk.RIGHT, padx=10, pady=10)
        
        input_label = tk.Label(left_frame, text="Select the directory with images")
        input_label.pack(anchor="center")

        self.input_dir_label = tk.Label(left_frame, text="", wraplength=500)
        self.input_dir_label.pack()

        input_dir_button = ttk.Button(left_frame, text="Select the directory", command=self.select_input_directory)
        input_dir_button.pack(pady=10)

        output_label = tk.Label(left_frame, text="Select the directory to save images:")
        output_label.pack(pady=10)

        self.output_dir_label = tk.Label(left_frame, text="", wraplength=500)
        self.output_dir_label.pack()

        output_dir_button = ttk.Button(left_frame, text="Select the directory", command=self.select_output_directory)
        output_dir_button.pack(pady=10)

        num_images_label = tk.Label(left_frame, text="Enter the number of images to create")
        num_images_label.pack()

        self.num_images_entry = ttk.Entry(left_frame)
        self.num_images_entry.pack(pady=10)

        resize_label = tk.Label(left_frame, text="Scaling (from 0 to 1):")
        resize_label.pack()
        self.resize_entry = ttk.Entry(left_frame)
        self.resize_entry.pack(pady=5)

        rotate_label = tk.Label(left_frame, text="Rotation (degrees):")
        rotate_label.pack()
        self.rotate_entry = ttk.Entry(left_frame)
        self.rotate_entry.pack(pady=5)

        brightness_label = tk.Label(left_frame, text="Brightness (1.0 - the original image):")
        brightness_label.pack()
        self.brightness_entry = ttk.Entry(left_frame)
        self.brightness_entry.pack(pady=5)

        contrast_label = tk.Label(left_frame, text="Contrast (1.0 - the original image):")
        contrast_label.pack()
        self.contrast_entry = ttk.Entry(left_frame)
        self.contrast_entry.pack(pady=5)

        saturation_label = tk.Label(left_frame, text="Saturation (1.0 - the original image):")
        saturation_label.pack()
        self.saturation_entry = ttk.Entry(left_frame)
        self.saturation_entry.pack(pady=5)

        self.crop_var = tk.IntVar()
        crop_checkbutton = ttk.Checkbutton(left_frame, text="Enable random cropping", variable=self.crop_var)
        crop_checkbutton.pack(pady=5)

        self.noise_var = tk.IntVar()
        noise_checkbutton = ttk.Checkbutton(left_frame, text="Add Gaussian Noise", variable=self.noise_var)
        noise_checkbutton.pack(pady=5)

        augment_button = ttk.Button(left_frame, text="Start augmentation", command=self.start_augmentation)
        augment_button.pack(pady=15)

        self.canvas = tk.Canvas(right_frame, width=350, height=600)
        self.canvas.pack()

    def display_image(self, image):
        """
        Displays the given image on the canvas.

        Parameters:
        image (PIL.Image): The image to display.
        """
        self.canvas.delete("all")

        image.thumbnail((350, 600), Image.LANCZOS)
        self.imgtk = ImageTk.PhotoImage(image)
        self.canvas.create_image(175, 300, image=self.imgtk)

    def select_input_directory(self):
        """
        Opens a dialog to select the input directory.
        """
        directory = filedialog.askdirectory()
        if directory:
            self.input_dir_label.config(text=directory)

            for file_name in os.listdir(directory):
                if file_name.lower().endswith(('jpg', 'jpeg', 'png')):
                    image_path = os.path.join(directory, file_name)
                    image = Image.open(image_path)
                    self.display_image(image)
                    break

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

        processor = ImageProcessor()

        def show_error(message):
            """
            Displays an error message.

            Parameters
            ----------
            message : str
                The error message to display.
            """
            messagebox.showerror("Error", message)

        if not input_dir or not output_dir:
            show_error("Fill in all the fields")
            return

        try:
            num_images = int(self.num_images_entry.get())
            if num_images <= 0:
                show_error("Number of images must be positive")
                return
        except ValueError:
            show_error("Number of images must be a valid integer")
            return
        

        try:
            resize = float(self.resize_entry.get() or 1)
            if not (0 <= resize <= 1):
                show_error("Resize value must be in range of 0 to 1")
                return
        except ValueError:
            show_error("Resize value must be a valid number")
            return

        
        try:
            rotate = int(self.rotate_entry.get() or 0)
        except ValueError:
            show_error("Rotation value must be a valid integer")
            return


        try:
            brightness_factor = float(self.brightness_entry.get() or 1.0)
        except ValueError:
            show_error("Brightness value must be a valid number")
            return
        

        try:
            contrast_factor = float(self.contrast_entry.get() or 1.0)
        except ValueError:
            show_error("Contrast value must be a valid number")
            return
        
        try:
            saturation_factor = float(self.saturation_entry.get() or 1.0)
        except ValueError:
            show_error("Saturation value must be a valid number")
            return
        
        random_crop = self.crop_var.get()

        add_noise = self.noise_var.get()

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        images = []
        for file_name in os.listdir(input_dir):
            if file_name.lower().endswith(('jpg', 'jpeg', 'png')):
                image_path = os.path.join(input_dir, file_name)
                image = Image.open(image_path)
                images.append(image)

        for i in range(num_images):
            for img in images:
                transformed_image = processor.apply_transformations(img, resize, rotate, brightness_factor, contrast_factor, saturation_factor, random_crop, add_noise)
                output_path = os.path.join(output_dir, f"augmented_{i}_{os.path.basename(img.filename)}")
                transformed_image.save(output_path)

                self.display_image(transformed_image)
                self.root.update()

