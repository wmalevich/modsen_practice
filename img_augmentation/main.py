from tkinter import Tk
from img_augmentation.augmentation import ImageAugmentationApp

def main():
    root = Tk()
    app = ImageAugmentationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()