from PIL import ImageEnhance

class ImageProcessor:
    @staticmethod
    def apply_transformations(img, resize, rotate, brightness_factor, contrast_factor, saturation_factor):
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

        if brightness_factor:
            img = ImageEnhance.Brightness(img)
            return img.enhance(brightness_factor)
        
        if brightness_factor:
            img = ImageEnhance.Brightness(img)
            return img.enhance(brightness_factor)
        
        if contrast_factor:
            img = ImageEnhance.Contrast(img)
            return img.enhance(contrast_factor)
        
        if saturation_factor:
            img = ImageEnhance.Color(img)
            return img.enhance(saturation_factor)

        return img
