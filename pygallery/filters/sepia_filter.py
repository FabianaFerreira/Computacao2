from pygallery.filter import Filter

import numpy as np
from skimage import color

class SepiaFilter(Filter):
    def __init__(self):
        super().__init__()
        self.name = 'Sepia'

    def apply(self, image):
        r, g, b = self.get_image_channels(image)

        # Referência:
        # https://www.techrepublic.com/blog/how-do-i/how-do-i-convert-images-to-grayscale-and-sepia-tone-using-c/
        new_r = np.clip((r * 0.393) + (g * 0.769) + (b * 0.189), 0, 1.0)
        new_g = np.clip((r * 0.349) + (g * 0.686) + (b * 0.168), 0, 1.0)
        new_b = np.clip((r * 0.272) + (g * 0.534) + (b * 0.131), 0, 1.0)

        new_img = self.merge_channels(new_r, new_g, new_b)
        return new_img
