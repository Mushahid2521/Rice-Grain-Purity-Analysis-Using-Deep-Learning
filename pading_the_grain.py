import numpy as np


def pad_image(img, size, value):

    # Measure difference from the desired width
    width = size-img.shape[0]
    # Check if even or odd
    if(width%2!=0):
        width_b = int(width/2)
        width_a = width_b+1
    else:
        width_b = int(width/2)
        width_a = width_b

    # check if even or odd
    height = size-img.shape[1]
    if(height%2!=0):
        height_b = int(height/2)
        height_a = height_b+1

    else:
        height_b = int(height/2)
        height_a = height_b

    # Padding with the folowing dimension
    pad_width = ((width_b,width_a),(height_b,height_a),(0,0))
    # Do padding
    img_new = np.pad(img, pad_width=pad_width, mode="constant", constant_values=value)

    return img_new


