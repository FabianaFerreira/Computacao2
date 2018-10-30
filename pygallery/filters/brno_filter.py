from pygallery.filter import Filter

import numpy as np
from skimage import color

class BrnoFilter(Filter):
	def __init__(self):
		super().__init__()

	def apply(self, image):
		h, s, v = self.get_image_hsv(image)

		new_img = self.merge_channels(np.clip(h - 0.05, 0, 1.0), s, v)

		# Small sharpening effect
		# sharp = self.sharpen(color.hsv2rgb(new_img), a=0.9, b=0.05, sigma=10)

		return color.hsv2rgb(new_img)
		