from PIL import ImageTk,Image
from tkinter import BOTH
from tkinter.ttk import Frame, Style

from image_frame import ImageFrame

class Gallery(Frame):
    def __init__(self, grid=(3,3), frame_size=300, frame_sep=50, margin=50):
        super().__init__()

        self.grid = (int(grid[0]), int(grid[1]))
        self.frame_size = frame_size
        self.frame_sep = frame_sep
        self.margin = margin
        self.images = []

        self.master.title("Gallery")
        self.pack(fill=BOTH, expand=True)
        Style().configure("TFrame", background="#333")

        self._setup_grid()

        self.bind("<Configure>", self._on_resize)

    def _setup_grid(self):
        for i in range(self.grid[0]):
            self.rowconfigure(i, pad=self.frame_sep)

        for i in range(self.grid[1]):
            self.columnconfigure(i, pad=self.frame_sep)

    def _get_frame_pos(self, index):
        row = int(index/self.grid[1])
        column = int(index % self.grid[1])
        #return (grid_x, grid_y)
        x_pos = int((self.frame_size + self.frame_sep) * column) + self.margin
        y_pos = int((self.frame_size + self.frame_sep) * row) + self.margin
        return (x_pos, y_pos)

    def _adjust_images_to_grid(self):
        for idx, img_frame in enumerate(self.images):
            pos = self._get_frame_pos(idx)
            img_frame.set_pos(pos)

    def _on_resize(self, event):
        width = event.width - 2*self.margin
        frames_w = int(width/self.frame_size)
        sep_w = int((width-frames_w*self.frame_size)/self.frame_sep)
        grid_columns = frames_w + (0 if sep_w >= (frames_w-1) else -1)

        heigth = event.height - 2*self.margin
        frames_h = int(heigth/self.frame_size)
        sep_h = int((heigth-frames_h*self.frame_size)/self.frame_sep)
        grid_rows = frames_h + (0 if sep_h >= (frames_h-1) else -1)

        new_grid = (grid_rows, grid_columns)
        if (new_grid != self.grid):
            self.grid = new_grid
            self._adjust_images_to_grid()

    def addImage(self, image_path):
        # TRATAR CASO DE GRID CHEIA
        image = Image.open(image_path)
        pos = self._get_frame_pos(len(self.images))
        img_frame = ImageFrame(self, image, pos=pos,
                               size=self.frame_size)
        self.images.append(img_frame)
