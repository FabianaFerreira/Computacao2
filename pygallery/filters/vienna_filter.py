from pygallery.filter import Filter

import numpy as np
from skimage import color

class ViennaFilter(Filter):
	def __init__(self):
		super().__init__()
		self.name = 'Vienna'

	def apply(self, image):
		h, s, v = self.get_image_hsv(image)

		new_img = self.merge_channels(h, np.clip(s - 0.3, 0, 1.0), v)

		# Small sharpening effect
		sharp = self.sharpen(color.hsv2rgb(new_img), a=0.9, b=0.05, sigma=10)

		return sharp
