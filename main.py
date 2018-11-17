import sys, os
sys.path.append(os.path.realpath("pygallery/"))

from tkinter import *
from pygallery import Gallery
from pygallery.filters import *

image_folder = os.path.realpath("images/")

from skimage import io, filters
import numpy as np

gui = Tk()
gui.geometry("800x800")
gallery = Gallery(frame_size=200)
gui.mainloop()
