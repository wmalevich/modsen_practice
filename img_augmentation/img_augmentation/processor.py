import random
from PIL import ImageEnhance, Image
import numpy as np

class ImageProcessor:
    @staticmethod
    def apply_transformations(img, resize, rotate, brightness_factor, contrast_factor, saturation_factor, random_crop, add_noise):
        """
        Applies resizing, rotation, brightness, contrast, and saturation transformations to an image.

        Parameters
        ----------
        img : PIL.Image.Image
            The image to be transformed.
        resize : float
            The factor by which to resize the image.
        rotate : float
            The angle by which to rotate the image.
        brightness_factor : float
            The factor by which to adjust brightness.
        contrast_factor : float
            The factor by which to adjust contrast.
        saturation_factor : float
            The factor by which to adjust saturation.
        random_crop : bool
            Wheter to apply random cropping

        Returns
        -------
        PIL.Image
            The transformed image.
        """
        if resize:
            width, height = img.size
            img = img.resize((int(width * resize), int(height * resize)))
        
        if rotate:
            img = img.rotate(rotate)
        
        if brightness_factor != 1:
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness_factor)

        if contrast_factor != 1:
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(contrast_factor)

        if saturation_factor != 1:
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(saturation_factor)
        
        if random_crop:
            img = ImageProcessor.random_crop(img)

        if add_noise:
            img = ImageProcessor.add_gaussian_noise(img)

        return img
    
    @staticmethod
    def random_crop(img):
        """
        Applies random cropping to the image.

        Parameters
        ----------
        img : PIL.Image.Image
            The image to be cropped.

        Returns
        -------
        PIL.Image
            The cropped image.
        """
        # Get the dimensions of the original image
        width, height = img.size

        # The new width and height are randomly selected between 50% and 100% of the original
        new_width = random.randint(int(width * 0.5), width)
        new_height = random.randint(int(height * 0.5), height)

        # Calculate the top-left corner
        left = random.randint(0, width - new_width)
        top = random.randint(0, height - new_height)

        # Calculate the bottom-right corner
        right = left + new_width
        bottom = right + new_height

        return img.crop((left, top, right, bottom))
    
    @staticmethod
    def add_gaussian_noise(img):
        """
        Adds Gaussian noise to the image.

        Parameters
        ----------
        img : PIL.Image.Image
            The image to which noise will be added.

        Returns
        -------
        PIL.Image
            The image with Gaussian noise.
        """
        # Convert to Numpy array
        img = np.array(img)

        # Define the mean and std
        mean = 0
        sigma = 25

        # Generate Gaussian noise
        gauss = np.random.normal(mean, sigma, img.shape).astype('uint8')

        # Add the Gaussian noise to the image
        noisy_img = img + gauss
        noisy_img = np.clip(noisy_img, 0, 255).astype('uint8')
        return Image.fromarray(noisy_img)