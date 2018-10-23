from tkinter import *
from tkinter.filedialog import askdirectory, askopenfilenames

from image_frame import ImageFrame
from gallery import Gallery

import os
image_folder = os.path.join(os.path.dirname(__file__), '../images/')

def get_images_from_list(file_list):
	img_regex = re.compile('.+\.(jpg|png)$')
	image_list = [file for file in file_list if img_regex.match(file)]
	return image_list

# CHECAR SE A LISTA DE IMAGENS ESTÁ VAZIA
def open_folder():
	folder = askdirectory(title='Selecione a pasta que contém suas imagens:')
	file_list = os.listdir(folder)
	return get_images_from_list(file_list)

# CHECAR SE A LISTA DE IMAGENS ESTÁ VAZIA
def open_files():
	file_list =  list(askopenfilenames(title = "Selecione a(s) imagem(ns):",
	                    filetypes = [("Arquivos JPEG, PNG","*.jpg *.png")]))
	return get_images_from_list(file_list)


gui = Tk()
gui.geometry("800x800")

#open_folder()
print(open_files())

# gallery = Gallery(frame_size=200, grid=(2,3))

# gallery.addImage(os.path.join(image_folder, 'landscape.jpg'))
# gallery.addImage(os.path.join(image_folder, 'chocolate.jpg'))
# gallery.addImage(os.path.join(image_folder, 'chocolate.jpg'))
# gallery.addImage(os.path.join(image_folder, 'putin.jpg'))
# gallery.addImage(os.path.join(image_folder, 'eiffel.jpg'))

gui.mainloop()
