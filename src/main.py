from tkinter import *

from image_frame import ImageFrame
from gallery import Gallery

import os
image_folder = os.path.join(os.path.dirname(__file__), '../images/')

gui = Tk()
gui.geometry("800x800")
gallery = Gallery(frame_size=200)
gui.mainloop()
