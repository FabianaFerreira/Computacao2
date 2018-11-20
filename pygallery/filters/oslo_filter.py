from pygallery.filter import Filter

import numpy as np
from skimage import color

class OsloFilter(Filter):
    def __init__(self):
        super().__init__()
        self.name = 'Oslo'

    def apply(self, image):
        width, height = image.shape[:2]

        xs = np.arange(width)
        ys = np.arange(height)
        distance_squared = (xs - width/2.0)[..., np.newaxis] ** 2 + (ys - height/2.0) ** 2

        sigma_squared = (width/2.0) ** 2 + (height/2.0) ** 2
        falloff = np.exp(-distance_squared/sigma_squared)

        r, g, b = self.get_image_channels(image)

        # Boost red mid-tones
        interp_vector = [0, 0.1, 0.2, 0.35, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 1.0]
        #               [0, 0.1,  0.2,  0.3, 0.4, 0.5, 0.6, 0.7, 0.8,  0.9, 1.0]
        r_boost_mid = self.interpolate_channel(r, interp_vector)

        # Boost green mid-tones
        interp_vector = [0, 0.15, 0.3, 0.38, 0.45, 0.55, 0.6, 0.7, 0.8, 0.9, 1.0]
        g_boost_mid = self.interpolate_channel(g, interp_vector)

        # Make blue less blue
        bluer_img = self.merge_channels(r_boost_mid, g_boost_mid, np.clip(b - 0.0, 0, 1.0))


        result = bluer_img * falloff[..., np.newaxis]
        return result
