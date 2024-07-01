import random
from PIL import ImageEnhance

class ImageProcessor:
    @staticmethod
    def apply_transformations(img, resize, rotate, brightness_factor, contrast_factor, saturation_factor, random_crop):
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
        width, height = img.size
        new_width = random.randint(int(width * 0.5), width)
        new_height = random.randint(int(height * 0.5), height)
        left = random.randint(0, width - new_width)
        top = random.randint(0, height - new_height)
        right = left + new_width
        bottom = right + new_height

        return img.crop((left, top, right, bottom))