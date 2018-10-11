from tkinter import *
from PIL import ImageTk,Image

class ImageFrame:
    def __init__(self, gallery, image, pos, size):
        if (not isinstance(pos, tuple)):
            raise TypeError('`pos` must be a tuple (x, y).')

        self.gallery = gallery
        self.image = image
        self.size = size

        self.imgTk = ImageTk.PhotoImage(self.resize_img_to_frame(self.image, self.size))

        self.label = Label(self.gallery, image=self.imgTk)
        self.label.image = self.imgTk
        self.pos = self._center_position(pos)
        self.label.place(x=self.pos[0], y=self.pos[1])
        self.label.bind("<Enter>", self._on_mouse_over)
        self.label.bind("<Leave>", self._on_mouse_leave)

    def _center_position(self, pos):
        center_x = pos[0] + int((self.size - self.imgTk.width())/2)
        center_y = pos[1] + int((self.size - self.imgTk.height())/2)
        return (center_x, center_y)

    def set_pos(self, pos):
        self.pos = self._center_position(pos)
        self.label.place(x=self.pos[0], y=self.pos[1])

    def _on_mouse_over(self, event):
        highlight_size = int(self.size*1.05)
        self.imgTk = ImageTk.PhotoImage(self.resize_img_to_frame(self.image, highlight_size))
        self.label.configure(image=self.imgTk)
        self.label.image = self.imgTk

    def _on_mouse_leave(self, event):
        self.imgTk = ImageTk.PhotoImage(self.resize_img_to_frame(self.image, self.size))
        self.label.configure(image=self.imgTk)
        self.label.image = self.imgTk

    def resize_img_to_frame(self, img, frame_size):
        if (img.size[0] > img.size[1]): # landscape mode image
            w_ratio = frame_size/float(img.size[0])
            new_width = frame_size
            new_height = int(img.size[1] * w_ratio)
        else: # portrait mode or square image
            h_ratio = frame_size/float(img.size[1])
            new_width = int(img.size[0] * h_ratio)
            new_height = frame_size
        return img.resize((new_width, new_height), Image.ANTIALIAS)
