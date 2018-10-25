from pygallery.filter import Filter

from skimage import color

class BWFilter(Filter):
	def __init__(self):
		super().__init__()

	def apply(self, image):
		return color.rgb2gray(image)