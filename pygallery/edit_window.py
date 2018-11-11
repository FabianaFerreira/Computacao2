from tkinter import Button, Frame, LEFT
from tkinter.ttk import Style

from screeninfo import get_monitors
from PIL import ImageTk, Image
from skimage import io

import matplotlib.pyplot as plt

from image_frame import ImageFrame
from filters import filter_list

class EditWindow:
    def __init__(self, window, image_path, margin=50):
        window.configure(background="#333") # background color
        self.window = window
        self.image_path = image_path
        self.margin = margin

        monitor = get_monitors()[0]
        self.width = monitor.width
        self.height = monitor.height

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

        self.__add_filter_buttons()

    def __add_filter_buttons(self):
        filters_frame = Frame(self.window, width=self.frame_size, height=100)
        filters_frame.place(x=self.margin, y=self.frame_size + self.margin)

        columns = 4
        for index, filter in enumerate(filter_list):
            row = int(index/columns)
            column = int(index % columns)
            btn = Button(filters_frame, text=filter.name,
                         command=lambda filter=filter: self.__apply_filter(filter))
            btn.grid(row=row, column=column, padx=10)

    def __apply_filter(self, filter):
        print("Applying filter " + filter.name)
        filt_image = filter.apply(self.originalFrame.image)
        self.filteredFrame.set_image(filt_image)
