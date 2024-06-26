from PIL import ImageEnhance

class ImageProcessor:
    """
    A class used to apply various transformations to images.

    Attributes
    ----------
    brightness_factor : float
        The factor by which to adjust brightness (default is 1.0)
    contrast_factor : float
        The factor by which to adjust contrast (default is 1.0)
    saturation_factor : float
        The factor by which to adjust saturation (default is 1.0)
    """

    def __init__(self):
        self.brightness_factor = 1.0
        self.contrast_factor = 1.0
        self.saturation_factor = 1.0
    
    def apply_transformations(self, img, resize, rotate):
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
        
        img = self.apply_brightness(img, self.brightness_factor)
        img = self.apply_contrast(img, self.contrast_factor)
        img = self.apply_saturation(img, self.saturation_factor)

        return img
    
    def apply_brightness(self, img, factor):
        """
        Applies brightness adjustment to an image.

        Parameters
        ----------
        img : PIL.Image.Image
            The image to be adjusted.
        factor : float
            The factor by which to adjust brightness.

        Returns
        -------
        PIL.Image.Image
            The brightness-adjusted image.
        """
        enhancer = ImageEnhance.Brightness(img)
        return enhancer.enhance(factor)
    
    def apply_contrast(self, img, factor):
        """
        Applies contrast adjustment to an image.

        Parameters
        ----------
        img : PIL.Image.Image
            The image to be adjusted.
        factor : float
            The factor by which to adjust contrast.

        Returns
        -------
        PIL.Image.Image
            The contrast-adjusted image.
        """
        enhancer = ImageEnhance.Contrast(img)
        return enhancer.enhance(factor)
    
    def apply_saturation(self, img, factor):
        """
        Applies saturation adjustment to an image.

        Parameters
        ----------
        img : PIL.Image.Image
            The image to be adjusted.
        factor : float
            The factor by which to adjust saturation.

        Returns
        -------
        PIL.Image.Image
            The saturation-adjusted image.
        """
        enhancer = ImageEnhance.Color(img)
        return enhancer.enhance(factor)

    def set_brightness(self, factor):
        """
        Sets the brightness factor for future transformations.

        Parameters
        ----------
        factor : float
            The factor by which to adjust brightness.
        """
        self.brightness_factor = factor
    
    def set_contrast(self, factor):
        """
        Sets the contrast factor for future transformations.

        Parameters
        ----------
        factor : float
            The factor by which to adjust contrast.
        """
        self.contrast_factor = factor
    
    def set_saturation(self, factor):
        """
        Sets the saturation factor for future transformations.

        Parameters
        ----------
        factor : float
            The factor by which to adjust saturation.
        """
        self.saturation_factor = factor
