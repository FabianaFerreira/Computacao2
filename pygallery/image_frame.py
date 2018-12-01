from tkinter import *

from PIL import ImageTk, Image
from skimage import io
import numpy as np


class ImageFrame:
    def __init__(self, gallery, image_path, pos, size,
                 hover=True, clickable=True):
        if (not isinstance(pos, tuple)):
            raise TypeError('`pos` must be a tuple (x, y).')

        self.gallery = gallery
        self.image_path = image_path
        # Open image with skimage and normalize the values between 0 and 1
        self.image = io.imread(image_path)/255.0
        self.size = size

        self.imgTk = ImageTk.PhotoImage(self.resize_img_to_frame(self.image, self.size))

        self.label = Label(self.gallery, image=self.imgTk)
        self.label.image = self.imgTk
        self.pos = self.__center_position(pos)
        self.label.place(x=self.pos[0], y=self.pos[1])

        if (hover):
            self.label.bind("<Enter>", self.__on_mouse_over)
            self.label.bind("<Leave>", self.__on_mouse_leave)

        if (clickable):
            self.label.bind("<Button-1>", self.__on_mouse_click)

    # Method to remove the ImageFrame
    def remove(self):
        self.label.place_forget()

    # Method to calculate the centered position of the ImageFrame
    def __center_position(self, pos):
        center_x = pos[0] + int((self.size - self.imgTk.width())/2)
        center_y = pos[1] + int((self.size - self.imgTk.height())/2)
        return (center_x, center_y)

    # Set position of the ImageFrame using `place`
    def set_pos(self, pos):
        self.pos = self.__center_position(pos)
        self.label.place(x=self.pos[0], y=self.pos[1])

    # Highlight the ImageFrame by expanding it
    def __on_mouse_over(self, event):
        # Fazer ser do centro pra fora
        highlight_size = int(self.size*1.05)
        self.imgTk = ImageTk.PhotoImage(self.resize_img_to_frame(self.image, highlight_size))
        self.label.configure(image=self.imgTk)
        self.label.image = self.imgTk

    # Return the ImageFrame to its original size
    def __on_mouse_leave(self, event):
        self.imgTk = ImageTk.PhotoImage(self.resize_img_to_frame(self.image, self.size))
        self.label.configure(image=self.imgTk)
        self.label.image = self.imgTk

    # Open the edit window to apply filters on the image.
    # It calls a method from Gallery because it needs the reference of the main
    # GUI to open a window
    def __on_mouse_click(self, event):
        self.gallery.open_edit_window(self.image_path)

    # Resize the image to fit in the frame
    def resize_img_to_frame(self, img_array, frame_size):
        img = Image.fromarray(np.uint8(img_array*255))
        if (img.size[0] > img.size[1]): # landscape mode image
            w_ratio = frame_size/float(img.size[0])
            new_width = frame_size
            new_height = int(img.size[1] * w_ratio)
        else: # portrait mode or square image
            h_ratio = frame_size/float(img.size[1])
            new_width = int(img.size[0] * h_ratio)
            new_height = frame_size
        return img.resize((new_width, new_height), Image.ANTIALIAS)

    # Set a new image
    def set_image(self, new_image):
        self.image = new_image
        self.imgTk = ImageTk.PhotoImage(self.resize_img_to_frame(self.image, self.size))
        self.label.configure(image=self.imgTk)
        self.label.image = self.imgTk
