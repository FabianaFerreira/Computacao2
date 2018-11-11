from pygallery.filter import Filter

import numpy as np
from skimage import color

class PyeongChangFilter(Filter):
	def __init__(self):
		super().__init__()
		self.name = 'PyeongChang'

	def apply(self, image):
		r, g, b = self.get_image_channels(image)

		# Boost red mid-tones
		# interp_vector = [0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9, 0.95, 1.0]
		# r_boost_lower = self.interpolate_channel(r, interp_vector)

		# Make blue a bit bluer
		bluer_img = self.merge_channels(r, g, np.clip(b + 0.3, 0, 1.0))

		# Small sharpening effect
		sharp = self.sharpen(bluer_img, a=1.3, b=0.3, sigma=10)

		# Split image again to interpolate the blue channel
		r, g, b = self.get_image_channels(sharp)
		interp_vector = [0, 0.047, 0.118, 0.251, 0.318, 0.392, 0.42, 0.439, 0.475, 0.561,
		                 0.58, 0.627, 0.671, 0.733, 0.847, 0.925, 1]
		b = self.interpolate_channel(b, interp_vector)

		return self.merge_channels(r, g, b)
