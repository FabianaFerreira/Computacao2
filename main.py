import sys, os
sys.path.append(os.path.realpath("pygallery/"))

from tkinter import *
from pygallery import Gallery
from pygallery.filters import *

image_folder = os.path.realpath("images/")

from skimage import io, filters
import matplotlib.pyplot as plt
import numpy as np

# img = io.imread(image_folder + '/landscape.jpg')/255.0

# a = 1.3
# b = 0.3
# blurred = filters.gaussian(img, sigma=10, multichannel=True)
# sharper = np.clip(img * a - blurred * b, 0, 1.0)

# #bw_filter = BWFilter()
# #bw_img = bw_filter.apply(img)
# #io.imshow(sharper)

# fig, axs = plt.subplots(1, 2)
# axs[0].imshow(img)
# axs[1].imshow(sharper)
#plt.show()


# gui = Tk()
# gui.geometry("800x800")
# gallery = Gallery(frame_size=200)
# gui.mainloop()

# def create_window():
#     window = Toplevel(root)
#     b = Label(window, text='Label dentro da janela')
#     b.pack()

# root = Tk()
# b = Button(root, text="Create new window", command=create_window)
# b.pack()

# root.mainloop()

img = io.imread(image_folder + '/landscape.jpg')/255.0
filter = GothamFilter() 
img_new = filter.apply(img)

# r, g, b = bw_filter.get_image_channels(img)
# r_interp = bw_filter.interpolate_channel(r, [0, 0.8, 1.0])
# img_new = bw_filter.merge_channels(r_interp, g, b)
fig, axs = plt.subplots(1, 2)
axs[0].imshow(img)
axs[1].imshow(img_new)
plt.show()
