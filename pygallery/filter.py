from skimage.filters import gaussian
from skimage.color import rgb2hsv
import numpy as np

class Filter:
	def __init__(self):
		pass

	def apply(self, image):
		pass

	# Split the image into red, green and blue channels
	def get_image_channels(self, image):
		red_channel = image[:, :, 0]
		green_channel = image[:, :, 1]
		blue_channel = image[:, :, 2]
		return red_channel, green_channel, blue_channel

	# Split the image into hue, saturation and value
	def get_image_hsv(self, image):
		image_hsv = rgb2hsv(image)
		hue = image_hsv[:, :, 0]
		saturation = image_hsv[:, :, 1]
		value = image_hsv[:, :, 2]
		return hue, saturation, value

	# Merge red, green and blue channels into an image
	def merge_channels(self, red, green, blue):
		return np.stack([red, green, blue], axis=2)

	# Apply a Gaussian filter to sharp the image
	def sharpen(self, image, a, b, sigma=10):
		blurred = gaussian(image, sigma=sigma, multichannel=True)
		return np.clip(image * a - blurred * b, 0, 1.0)

	# Apply a linear interpolation given a channel and the interpolation values
	def interpolate_channel(self, channel, values):
		channel_shape = channel.shape
		flat_matrix = channel.flatten()
		interpolated = np.interp(flat_matrix,
			                     np.linspace(0, 1.0, len(values)),
			                     values)

		return interpolated.reshape(channel_shape)
