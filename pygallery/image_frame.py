import numpy as np

from tkinter import *
from PIL import ImageTk, Image
from skimage import io


class ImageFrame:
    def __init__(self, gallery, image_path, pos, size,
                 hover=True, clickable=True):
        if (not isinstance(pos, tuple)):
            raise TypeError('`pos` must be a tuple (x, y).')

        self.gallery = gallery
        self.image_path = image_path
        #self.image = Image.open(image_path)
        self.image = io.imread(image_path)/255.0
        self.size = size

        self.imgTk = ImageTk.PhotoImage(self.resize_img_to_frame(self.image, self.size))

        self.label = Label(self.gallery, image=self.imgTk)
        self.label.image = self.imgTk
        self.pos = self.__center_position(pos)
        #self.label.place(x=self.pos[0], y=self.pos[1])
        self.label.grid(row=self.pos[0], column=self.pos[1], sticky=W+E+N+S)

        if (hover):
            self.label.bind("<Enter>", self.__on_mouse_over)
            self.label.bind("<Leave>", self.__on_mouse_leave)

        if (clickable):
            self.label.bind("<Button-1>", self.__on_mouse_click)

    def remove(self):
        self.label.place_forget()

    def __center_position(self, pos):
        center_x = pos[0] + int((self.size - self.imgTk.width())/2)
        center_y = pos[1] + int((self.size - self.imgTk.height())/2)
        return (center_x, center_y)

    def set_pos(self, pos):
        self.pos = self.__center_position(pos)
        self.label.place(x=self.pos[0], y=self.pos[1])

    def __on_mouse_over(self, event):
        # Fazer ser do centro pra fora
        highlight_size = int(self.size*1.05)
        self.imgTk = ImageTk.PhotoImage(self.resize_img_to_frame(self.image, highlight_size))
        self.label.configure(image=self.imgTk)
        self.label.image = self.imgTk

    def __on_mouse_leave(self, event):
        self.imgTk = ImageTk.PhotoImage(self.resize_img_to_frame(self.image, self.size))
        self.label.configure(image=self.imgTk)
        self.label.image = self.imgTk

    def __on_mouse_click(self, event):
        self.gallery.open_edit_window(self.image_path)

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

    def set_image(self, new_image):
        self.image = new_image
        self.imgTk = ImageTk.PhotoImage(self.resize_img_to_frame(self.image, self.size))
        self.label.configure(image=self.imgTk)
        self.label.image = self.imgTk
