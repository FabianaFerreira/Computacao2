import os
import re
from PIL import Image
from tkinter import BOTH, Menu, Toplevel, messagebox
from tkinter.ttk import Frame, Style
from tkinter.filedialog import askdirectory, askopenfilenames

from image_frame import ImageFrame
from edit_window import EditWindow

def get_images_from_list(file_list):
        img_regex = re.compile('.+\.(jpg|png)$')
        return [file for file in file_list if img_regex.match(file)]

class Gallery(Frame):
    def __init__(self, grid=(3,3), frame_size=200, frame_sep=50, margin=50):
        super().__init__()

        self.grid = (int(grid[0]), int(grid[1]))
        self.frame_size = frame_size
        self.frame_sep = frame_sep
        self.margin = margin
        self.image_frames = []

        self.master.title("Gallery")
        self.pack(fill=BOTH, expand=True)
        Style().configure("TFrame", background="#333") # background color

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        # Add menu options to open image or folder
        fileMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Abrir imagem...", command=self.open_files)
        fileMenu.add_command(label="Abrir pasta...", command=self.open_folder)
        menubar.add_cascade(label="Arquivo", menu=fileMenu)

        # Window resize event
        self.bind("<Configure>", self._on_resize)

    def _get_frame_pos(self, index):
        # If the grid is full, add one more line
        if (index >= (self.grid[0] * self.grid[1])):
            self.grid = (self.grid[0] + 1, self.grid[1])

        # Calculate the row and column indexes
        row = int(index/self.grid[1])
        column = int(index % self.grid[1])

        # Calculate the image position based on its indexes
        x_pos = int((self.frame_size + self.frame_sep) * column) + self.margin
        y_pos = int((self.frame_size + self.frame_sep) * row) + self.margin
        return (x_pos, y_pos)

    def _adjust_images_to_grid(self):
        # Recalculate the image positions based on the grid size
        for idx, img_frame in enumerate(self.image_frames):
            pos = self._get_frame_pos(idx)
            img_frame.set_pos(pos)

    def _on_resize(self, event):
        # Calculate the new amount of columns based on the window size
        width = event.width - 2*self.margin
        frames_w = int(width/self.frame_size)
        sep_w = int((width-frames_w*self.frame_size)/self.frame_sep)
        grid_columns = frames_w + (0 if sep_w >= (frames_w-1) else -1)

        # Calculate the new amount of rows based on the window size
        heigth = event.height - 2*self.margin
        frames_h = int(heigth/self.frame_size)
        sep_h = int((heigth-frames_h*self.frame_size)/self.frame_sep)
        grid_rows = frames_h + (0 if sep_h >= (frames_h-1) else -1)

        new_grid = (grid_rows, grid_columns)
        # If the new_grid is different from the current one,
        # then adjust the images to the new grid
        if (new_grid != self.grid):
            self.grid = new_grid
            self._adjust_images_to_grid()

    # Add an ImageFrame with the image specified by `image_path`
    def addImage(self, image_path):
        pos = self._get_frame_pos(len(self.image_frames))
        img_frame = ImageFrame(self, image_path, pos=pos,
                               size=self.frame_size)
        self.image_frames.append(img_frame)

    # Open a folder containing images and add them to the grid
    def open_folder(self):
        folder = askdirectory(title='Selecione a pasta que contém suas imagens:')
        if (not folder):
            return
        file_list = os.listdir(folder)
        image_list = [folder + "/" + image for image in get_images_from_list(file_list)]
        if (image_list):
            if (self.image_frames):
                self.clearGallery()
            self.image_list = image_list
            for image in image_list:
                self.addImage(image)
        else:
            messagebox.showerror("Erro",
                                 "Nenhuma imagem encontrada na pasta selecionada.")

    # Open one or multiple images and add them to the grid
    def open_files(self):
        file_list =  list(askopenfilenames(title="Selecione a(s) imagem(ns):",
                                           filetypes=[("Arquivos JPEG, PNG","*.jpg *.png")]))
        if (not file_list):
            return
        image_list = get_images_from_list(file_list)
        if (image_list):
            if (self.image_frames):
                self.clearGallery()
            self.image_list = image_list
            for image in image_list:
                self.addImage(image)
        else:
            messagebox.showerror("Erro",
                                 "Nenhum arquivo de imagem foi selecionado.")

    # Delete all the images from the grid
    def clearGallery(self):
        for image_frame in self.image_frames:
            image_frame.remove()
            del image_frame
        self.image_frames = []

    # Open the edit window upon clicking on an image
    def open_edit_window(self, image_path):
        window = Toplevel(self)
        window.geometry("1280x768")
        window.update_idletasks()
        edit_window_obj = EditWindow(window, image_path)
