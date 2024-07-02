import unittest
from PIL import Image, ImageEnhance
from img_augmentation.processor import ImageProcessor

class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.img = Image.new('RGB', (100, 100), color = 'red')
    
    def test_resize(self):
        result_img = ImageProcessor.apply_transformations(self.img, resize=0.5, rotate=0, brightness_factor=1, contrast_factor=1, saturation_factor=1, random_crop=False)
        self.assertEqual(result_img.size, (50, 50))
    
    def test_rotate(self):
        result_img = ImageProcessor.apply_transformations(self.img, resize=1, rotate=45, brightness_factor=1, contrast_factor=1, saturation_factor=1, random_crop=False)
        self.assertEqual(result_img.size, (100, 100))
    
    def test_brightness(self):
        result_img = ImageProcessor.apply_transformations(self.img, resize=1, rotate=0, brightness_factor=2, contrast_factor=1, saturation_factor=1, random_crop=False)
        enhancer = ImageEnhance.Brightness(self.img)
        expected_img = enhancer.enhance(2)
        self.assertTrue(list(result_img.getdata()) == list(expected_img.getdata()))
    
    def test_contrast(self):
        result_img = ImageProcessor.apply_transformations(self.img, resize=1, rotate=0, brightness_factor=1, contrast_factor=2, saturation_factor=1, random_crop=False)
        enhancer = ImageEnhance.Contrast(self.img)
        expected_img = enhancer.enhance(2)
        self.assertTrue(list(result_img.getdata()) == list(expected_img.getdata()))
    
    def test_saturation(self):
        result_img = ImageProcessor.apply_transformations(self.img, resize=1, rotate=0, brightness_factor=1, contrast_factor=1, saturation_factor=2, random_crop=False)
        enhancer = ImageEnhance.Color(self.img)
        expected_img = enhancer.enhance(5)
        self.assertTrue(list(result_img.getdata()) == list(expected_img.getdata()))

    def test_random_crop(self):
        result_img = ImageProcessor.apply_transformations(self.img, resize=1, rotate=0, brightness_factor=1, contrast_factor=1, saturation_factor=1, random_crop=True)
        self.assertLessEqual(result_img.size, self.img.size)


if __name__ == '__main__':
    unittest.main()
