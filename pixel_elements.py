# SH-I: pixel_elements.py

import numpy as np
import matplotlib.pyplot as plt

# RGB Colors
blue = (0, 144, 188)
green = (0, 166, 81)
yellow = (255, 212, 0)
purple = (165, 67, 153)
lightblue = (143, 204, 233)
red = (237, 28, 36)
black = (0, 0, 0)
grey = (188, 188, 188)

# Blank Canvas
def make_canvas():
    """Makes a 5x5 pixel white canvas."""
    return np.full((5, 5, 3), 255, dtype = int)

# Vertical Stick
def vert_stick(link = 'a', occu = None):
    """Draws a vertical stick.
    link: Type of linkage. ['a', 'b']
    occu: Position occupied. ['2', '3', '4', '5', '6']
    """
    drawing = make_canvas()
    color = grey if (link == 'b') else black
    for i, c in enumerate(color):
        drawing[:, :, i][:, 2] = c
    occu_list = ['2', '3', '4', '5', '6']
    if occu in occu_list:
        o = occu_list.index(occu)
        for i, c in enumerate(red):
            drawing[:, :, i][o, 2] = c
    return drawing

# Horizontal Stick
def horz_stick(link = 'a', occu = None):
    """Draws a horizontal stick.
    link: Type of linkage. ['a', 'b']
    occu: Position occupied. ['2', '3', '4', '5', '6']
    """
    drawing = make_canvas()
    color = grey if (link == 'b') else black
    for i, c in enumerate(color):
        drawing[:, :, i][2, :] = c
    occu_list = ['2', '3', '4', '5', '6']
    if occu in occu_list:
        o = occu_list.index(occu)
        for i, c in enumerate(red):
            drawing[:, :, i][2, o] = c
    return drawing

# Left Diagonal Stick
def left_diag_stick(link = 'a', occu = None):
    """Draws a left diagonal stick.
    link: Type of linkage. ['a', 'b']
    occu: Position occupied. ['2', '3', '4', '5', '6']
    """
    drawing = make_canvas()
    color = grey if (link == 'b') else black
    for i, c in enumerate(color):
        for j in range(5):
            drawing[:, :, i][j, j] = c
            drawing[:, :, i][j, j] = c
            drawing[:, :, i][j, j] = c
    occu_list = ['2', '3', '4', '5', '6']
    if occu in occu_list:
        o = occu_list.index(occu)
        for i, c in enumerate(red):
            drawing[:, :, i][o, o] = c
    return drawing

# Right Diagnoal Stick
def right_diag_stick(link = 'a', occu = None):
    """Draws a right diagnol stick stick.
    link: Type of linkage. ['a', 'b']
    occu: Position occupied. ['2', '3', '4', '5', '6']
    """
    drawing = make_canvas()
    color = grey if (link == 'b') else black
    for i, c in enumerate(color):
        for j in range(5):
            drawing[:, :, i][4 - j, j] = c
            drawing[:, :, i][4 - j, j] = c
            drawing[:, :, i][4 - j, j] = c
    occu_list = ['2', '3', '4', '5', '6']
    if occu in occu_list:
        o = occu_list.index(occu)
        for i, c in enumerate(red):
            drawing[:, :, i][4 - o, o] = c
    return drawing

# Glucose
Glc = make_canvas()
for i, c in enumerate(blue):
    Glc[:, :, i][:, 1:-1] = c
    Glc[:, :, i][1:-1, :] = c

# Mannose
Man = make_canvas()
for i, c in enumerate(green):
    Man[:, :, i][:, 1:-1] = c
    Man[:, :, i][1:-1, :] = c

# Galactose
Gal = make_canvas()
for i, c in enumerate(yellow):
    Gal[:, :, i][:, 1:-1] = c
    Gal[:, :, i][1:-1, :] = c

# N-Acetyl Glucosamine
GlcNAc = make_canvas()
for i, c in enumerate(blue):
    GlcNAc[:, :, i] = c

# N-Acetyl Galactosamine
GalNAc = make_canvas()
for i, c in enumerate(yellow):
    GalNAc[:, :, i] = c

# Galacturonic Acid
GlcA = make_canvas()
for i, c in enumerate(blue):
    GlcA[:, :, i][:, 2] = c
    GlcA[:, :, i][1:-1, 1:-1] = c
    GlcA[:, :, i][2, :] = c
for i, c in enumerate(black):
    GlcA[:, :, i][3, 1:-1] = c
    GlcA[:, :, i][4, 2] = c

# N-Acetylneuraminic Acid
Neu5Ac = make_canvas()
for i, c in enumerate(purple):
    Neu5Ac[:, :, i][:, 2] = c
    Neu5Ac[:, :, i][1:-1, 1:-1] = c
    Neu5Ac[:, :, i][2, :] = c

# N-Glycolylneuraminic Acid
Neu5Gc = make_canvas()
for i, c in enumerate(lightblue):
    Neu5Gc[:, :, i][:, 2] = c
    Neu5Gc[:, :, i][1:-1, 1:-1] = c
    Neu5Gc[:, :, i][2, :] = c

# Fucose
Fuc = make_canvas()
for i, c in enumerate(red):
    Fuc[:, :, i][:, 0] = c
    Fuc[:, :, i][1:-1, 1] = c
    Fuc[:, :, i][2, 2] = c
