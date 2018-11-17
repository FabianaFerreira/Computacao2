from tkinter import Button, Frame, LEFT, RIGHT, BOTTOM
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
        print(self.width)


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

        buttons_frame = Frame(self.window, width=self.frame_size, height=100,
                              bd=5, padx=10, pady=10)
        buttons_frame.place(x=self.frame_size + self.margin/2.0,
                            y=self.frame_size + self.margin/2.0)
        #buttons_frame.pack(side=BOTTOM)
        btn = Button(buttons_frame, text="Salvar como", command=self.save)
        btn.pack(side=RIGHT)

        btn = Button(buttons_frame, text="Cancelar", command=self.close)
        btn.pack()

    def __add_filter_buttons(self):
        filters_frame = Frame(self.window, width=self.frame_size, height=100,
                              bd=5, padx=10, pady=10)
        filters_frame.place(x=self.margin, y=self.frame_size + self.margin/2.0)

        columns = 8
        for index, filter in enumerate(filter_list):
            row = int(index/columns)
            column = int(index % columns)
            btn = Button(filters_frame, text=filter.name,
                         command=lambda filter=filter: self.__apply_filter(filter))
            btn.grid(row=row, column=column, ipadx=5)

    def __apply_filter(self, filter):
        filt_image = filter.apply(self.originalFrame.image)
        self.filteredFrame.set_image(filt_image)

    def save(self):
        initial_dir = dirname(self.image_path)
        filename = asksaveasfilename(initialdir=initial_dir,
                                     title="Salvar imagem",
                                     filetypes=[("Arquivos JPEG, PNG","*.jpg *.png")])
        if (filename):
            io.imsave(filename, self.filteredFrame.image)
            self.window.destroy()

    def close(self):
        self.window.destroy()
