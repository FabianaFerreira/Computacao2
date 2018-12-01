from tkinter import *
from tkinter.ttk import Style
from tkinter.filedialog import asksaveasfilename

from os.path import dirname
from PIL import ImageTk, Image
from skimage import io

from image_frame import ImageFrame
from filters import filter_list

class EditWindow:
    def __init__(self, window, image_path, margin=50):
        window.configure(background="#333") # background color
        self.window = window
        self.image_path = image_path
        self.margin = margin

        self.width = window.winfo_width()
        self.height = window.winfo_height()

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

        # Add the filter buttons
        self.__add_filter_buttons()

        # Add the save and cancel buttons
        buttons_frame = Frame(self.window, width=self.frame_size, height=100)
        buttons_frame.configure(background="#333")
        buttons_frame.place(x=int(self.frame_size*1.5) + int(self.margin/2.0) + 25,
                            y=self.frame_size + int(self.margin/2.0))

        btn = Button(buttons_frame, text="Salvar como",
                     width=10, command=self.save)
        btn.pack()

        btn = Button(buttons_frame, text="Cancelar",
                     width=10, command=self.close)
        btn.pack()

    def __add_filter_buttons(self):
        filters_frame = Frame(self.window, width=self.frame_size, height=100)
        filters_frame.configure(background="#333")
        filters_frame.place(x=self.margin + 50, y=self.frame_size + int(self.margin/2.0))

        columns = 4
        for index, filter in enumerate(filter_list):
            row = int(index/columns)
            column = int(index % columns)
            btn = Button(filters_frame, text=filter.name,
                         width=10,
                         command=lambda filter=filter: self.__apply_filter(filter))
            btn.grid(row=row, column=column, ipadx=10)

    # Apply the selected filter to the image
    def __apply_filter(self, filter):
        filt_image = filter.apply(self.originalFrame.image)
        self.filteredFrame.set_image(filt_image)

    # Save the filtered image
    def save(self):
        initial_dir = dirname(self.image_path)
        filename = asksaveasfilename(initialdir=initial_dir,
                                     title="Salvar imagem",
                                     filetypes=[("Arquivos JPEG, PNG","*.jpg *.png")])
        if (filename):
            io.imsave(filename, self.filteredFrame.image)
            self.close()

    # Close the edit window
    def close(self):
        self.window.destroy()
