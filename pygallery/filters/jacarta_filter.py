from pygallery.filter import Filter

import numpy as np
from skimage import color

class JacartaFilter(Filter):
    def __init__(self):
        super().__init__()
        self.name = 'Jacarta'

    def apply(self, image):
        h, s, v = self.get_image_hsv(image)
        new_hsv = self.merge_channels(np.clip(h + 0.04, 0, 1.0),
                                      np.clip(s - 0.05, 0, 1.0),
                                      np.clip(v + 0.0, 0, 1.0))
        return color.hsv2rgb(new_hsv)
