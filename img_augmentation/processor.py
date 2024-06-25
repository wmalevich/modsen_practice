from PIL import ImageEnhance

class ImageProcessor:
    def __init__(self):
        self.brightness_factor = 1.0
        self.contrast_factor = 1.0
        self.saturation_factor = 1.0
    
    def apply_transformations(self, img, resize, rotate):
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
        enhancer = ImageEnhance.Brightness(img)
        return enhancer.enhance(factor)
    
    def apply_contrast(self, img, factor):
        enhancer = ImageEnhance.Contrast(img)
        return enhancer.enhance(factor)
    
    def apply_saturation(self, img, factor):
        enhancer = ImageEnhance.Color(img)
        return enhancer.enhance(factor)

    def set_brightness(self, factor):
        self.brightness_factor = factor
    
    def set_contrast(self, factor):
        self.contrast_factor = factor
    
    def set_saturation(self, factor):
        self.saturation_factor = factor


