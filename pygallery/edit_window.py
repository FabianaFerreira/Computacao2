from tkinter import Button, BOTTOM
from screeninfo import get_monitors
from PIL import ImageTk, Image
from skimage import io

import matplotlib.pyplot as plt

from image_frame import ImageFrame
from filters import filters_dict

class EditWindow:
    def __init__(self, window, image_path, margin=50):
        self.window = window
        monitor = get_monitors()[0]
        self.width = monitor.width
        self.height = monitor.height

        self.image_path = image_path
        # self.image = io.imread(image_path)/255.0
        # self.filt_image = self.image.copy()

        self.frame_size = int((self.width - 3*margin)/2)

        pos = (margin, 0)
        self.originalFrame = ImageFrame(self.window,
                                        self.image_path,
                                        pos=pos,
                                        size=self.frame_size,
                                        hover=False,
                                        clickable=False)

        pos = (self.frame_size + 2*margin, 0)
        self.filteredFrame = ImageFrame(self.window,
                                        self.image_path,
                                        pos=pos,
                                        size=self.frame_size,
                                        hover=False,
                                        clickable=False)


        btn = Button(window, text="BW", command=lambda: self.apply_filter("bw"))
        btn.pack(side=BOTTOM)

        btn = Button(window, text="Brno", command=lambda: self.apply_filter("brno"))
        btn.pack(side=BOTTOM)

    def apply_filter(self, filter_name):
        filter = filters_dict[filter_name]
        filt_image = filter.apply(self.originalFrame.image)
        self.filteredFrame.set_image(filt_image)
