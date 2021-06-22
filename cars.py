import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly
from tkinter import filedialog
from tkinter import *
import os

#imagenguard = input('''Ingrese el nombre de la imagen en su Biblioteca de Imagenes: ''')
imagenguard = filedialog.askopenfilename(initialdir = "/", title="Select a Image File", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
Button(text="Open File", bg="pale green", command=imagenguard).place(x=10, y=10)
image = cv2.imread(imagenguard)
box, label, count = cv.detect_common_objects(image)
output = draw_bbox(image, box, label, count)
plt.imshow(output)
plt.show()
print("Total number of cars are: "+str(label.count('car')))

